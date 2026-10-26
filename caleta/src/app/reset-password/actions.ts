'use server'

import { createClient } from '@/utils/supabase/server'
import { redirect } from 'next/navigation'

export async function resetPassword(formData: FormData) {
  const supabase = await createClient()
  const password = formData.get('password') as string

  if (!password) {
    return { error: 'La contraseña es requerida.' }
  }

  const { error } = await supabase.auth.updateUser({
    password,
  })

  if (error) {
    return { error: error.message }
  }

  redirect('/bienvenida')
}
