'use server'

import { createClient } from '@/utils/supabase/server'
import { headers } from 'next/headers'

export async function requestPasswordReset(formData: FormData) {
  const supabase = await createClient()
  const origin = (await headers()).get('origin')
  const email = formData.get('email') as string

  if (!email) {
    return { error: 'El correo es requerido.' }
  }

  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${origin}/auth/callback?next=/reset-password`,
  })

  if (error) {
    return { error: error.message }
  }

  return { success: true }
}
