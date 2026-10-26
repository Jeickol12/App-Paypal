'use client'

import { useState } from 'react'
import Link from 'next/link'
import { signup } from '@/app/login/actions'
import { CheckCircle2 } from 'lucide-react'

export default function RegisterPage() {
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(false)

  async function handleSubmit(formData: FormData) {
    setLoading(true)
    setError('')
    const res = await signup(formData)
    
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
          <h2 className="text-2xl font-bold text-slate-900 mb-2">¡Revisa tu correo!</h2>
          <p className="text-slate-600 mb-6">
            Te hemos enviado un enlace para confirmar tu cuenta. Haz clic en él para poder iniciar sesión.
          </p>
          <Link href="/login" className="inline-block bg-teal-600 text-white font-medium px-6 py-2 rounded-lg hover:bg-teal-700 transition-colors">
            Ir a Iniciar Sesión
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="flex-1 flex flex-col justify-center items-center p-6 py-12">
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
        <div className="text-center mb-8">
          <Link href="/" className="text-2xl font-bold text-slate-900 inline-block mb-2">
            Caleta <span className="text-teal-600">.</span>
          </Link>
          <h1 className="text-2xl font-semibold text-slate-800">Crea tu cuenta</h1>
          <p className="text-slate-500 mt-2">Únete a la plataforma global de cobros</p>
        </div>

        <form action={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1" htmlFor="full_name">Nombre completo o Razón Social</label>
            <input
              id="full_name"
              name="full_name"
              type="text"
              required
              className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-colors outline-none"
              placeholder="Ej. Juan Pérez"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1" htmlFor="account_type">Tipo de cuenta</label>
            <select
              id="account_type"
              name="account_type"
              required
              className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-colors outline-none bg-white"
            >
              <option value="freelancer">Freelancer (Persona Natural)</option>
              <option value="business">Empresa (PYME registrada)</option>
            </select>
          </div>

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
          
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1" htmlFor="password">Contraseña</label>
            <input
              id="password"
              name="password"
              type="password"
              required
              minLength={6}
              className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-colors outline-none"
              placeholder="Mínimo 6 caracteres"
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
            className="w-full bg-teal-600 text-white font-medium py-2.5 rounded-lg hover:bg-teal-700 transition-colors disabled:opacity-70 disabled:cursor-not-allowed flex justify-center items-center mt-2"
          >
            {loading ? 'Registrando...' : 'Registrarse'}
          </button>
        </form>

        <p className="text-center text-sm text-slate-600 mt-8">
          ¿Ya tienes una cuenta? <Link href="/login" className="text-teal-600 font-medium hover:text-teal-700">Inicia sesión</Link>
        </p>
      </div>
    </div>
  )
}
