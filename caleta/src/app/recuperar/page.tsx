'use client'

import { useState } from 'react'
import Link from 'next/link'
import { requestPasswordReset } from './actions'
import { CheckCircle2 } from 'lucide-react'

export default function RecoverPage() {
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(false)

  async function handleSubmit(formData: FormData) {
    setLoading(true)
    setError('')
    const res = await requestPasswordReset(formData)
    
    if (res?.error) {
      setError(res.error)
      setLoading(false)
    } else if (res?.success) {
      setSuccess(true)
      setLoading(false)
    }
  }

  if (success) {
    return (
      <div className="flex-1 flex flex-col justify-center items-center p-6">
        <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-sm border border-slate-200 text-center">
          <CheckCircle2 className="w-16 h-16 text-teal-600 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-slate-900 mb-2">Correo enviado</h2>
          <p className="text-slate-600 mb-6">
            Si el correo está registrado en nuestra plataforma, recibirás un enlace para restablecer tu contraseña.
          </p>
          <Link href="/login" className="inline-block bg-teal-600 text-white font-medium px-6 py-2 rounded-lg hover:bg-teal-700 transition-colors">
            Volver a Iniciar Sesión
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="flex-1 flex flex-col justify-center items-center p-6">
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
        <div className="text-center mb-8">
          <Link href="/" className="text-2xl font-bold text-slate-900 inline-block mb-2">
            Caleta <span className="text-teal-600">.</span>
          </Link>
          <h1 className="text-xl font-semibold text-slate-800">Recupera tu cuenta</h1>
          <p className="text-slate-500 mt-2 text-sm">Ingresa tu correo y te enviaremos un enlace para restablecer tu contraseña.</p>
        </div>

        <form action={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1" htmlFor="email">Correo electrónico</label>
            <input
              id="email"
              name="email"
              type="email"
              required
              className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-colors outline-none"
              placeholder="tu@correo.com"
            />
          </div>

          {error && (
            <div className="bg-red-50 text-red-600 text-sm p-3 rounded-lg border border-red-100">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-teal-600 text-white font-medium py-2.5 rounded-lg hover:bg-teal-700 transition-colors disabled:opacity-70 disabled:cursor-not-allowed"
          >
            {loading ? 'Enviando...' : 'Enviar enlace'}
          </button>
        </form>

        <p className="text-center text-sm text-slate-600 mt-8">
          <Link href="/login" className="text-teal-600 font-medium hover:text-teal-700">Volver a iniciar sesión</Link>
        </p>
      </div>
    </div>
  )
}
