-- Crea una tabla para los perfiles públicos de los usuarios
create table public.profiles (
  id uuid references auth.users on delete cascade not null primary key,
  full_name text,
  account_type text check (account_type in ('freelancer', 'business')),
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Habilitar Row Level Security (RLS)
alter table public.profiles enable row level security;

-- Política 1: Los usuarios pueden ver su propio perfil
create policy "Usuarios pueden ver su propio perfil" on public.profiles
  for select using (auth.uid() = id);

-- Política 2: Los usuarios pueden actualizar su propio perfil
create policy "Usuarios pueden actualizar su propio perfil" on public.profiles
  for update using (auth.uid() = id);

-- Función para insertar automáticamente un perfil cuando un usuario se registra
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, full_name, account_type)
  values (
    new.id,
    new.raw_user_meta_data->>'full_name',
    new.raw_user_meta_data->>'account_type'
  );
  return new;
end;
$$ language plpgsql security definer;

-- Trigger para ejecutar la función cuando se crea un usuario en auth.users
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
