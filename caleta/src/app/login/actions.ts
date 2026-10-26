'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'
import { createClient } from '@/utils/supabase/server'

export async function login(formData: FormData) {
  const supabase = await createClient()

  // type-casting here for convenience
  // in practice, you should validate your inputs
  const email = formData.get('email') as string
  const password = formData.get('password') as string

  if (!email || !password) {
    return { error: 'Faltan campos requeridos.' }
  }

  const { error } = await supabase.auth.signInWithPassword({
    email,
    password,
  })

  if (error) {
    // Para seguridad, no revelar si el correo existe o no, mensaje genérico.
    return { error: 'Credenciales inválidas o correo no confirmado.' }
  }

  revalidatePath('/', 'layout')
  redirect('/bienvenida')
}

export async function signup(formData: FormData) {
  const supabase = await createClient()

  const email = formData.get('email') as string
  const password = formData.get('password') as string
  const fullName = formData.get('full_name') as string
  const accountType = formData.get('account_type') as string

  if (!email || !password || !fullName || !accountType) {
    return { error: 'Por favor, completa todos los campos.' }
  }

  const { error, data } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: {
        full_name: fullName,
        account_type: accountType,
      },
    },
  })

  if (error) {
    return { error: error.message }
  }

  return { success: true, message: 'Revisa tu correo para confirmar tu registro.' }
}

export async function logout() {
  const supabase = await createClient()
  await supabase.auth.signOut()
  redirect('/login')
}
