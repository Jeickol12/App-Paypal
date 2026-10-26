'use client'

import { useState } from 'react'
import Link from 'next/link'
import { login } from './actions'

export default function LoginPage() {
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(formData: FormData) {
    setLoading(true)
    setError('')
    const res = await login(formData)
    if (res?.error) {
      setError(res.error)
      setLoading(false)
    }
  }

  return (
    <div className="flex-1 flex flex-col justify-center items-center p-6">
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
        <div className="text-center mb-8">
          <Link href="/" className="text-2xl font-bold text-slate-900 inline-block mb-2">
            Caleta <span className="text-teal-600">.</span>
          </Link>
          <h1 className="text-2xl font-semibold text-slate-800">Inicia sesión</h1>
          <p className="text-slate-500 mt-2">Accede a tu cuenta para continuar</p>
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
          <div>
            <div className="flex justify-between items-center mb-1">
              <label className="block text-sm font-medium text-slate-700" htmlFor="password">Contraseña</label>
              <Link href="/recuperar" className="text-sm text-teal-600 hover:text-teal-700">¿Olvidaste tu contraseña?</Link>
            </div>
            <input
              id="password"
              name="password"
              type="password"
              required
              className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-colors outline-none"
              placeholder="••••••••"
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
            className="w-full bg-teal-600 text-white font-medium py-2.5 rounded-lg hover:bg-teal-700 transition-colors disabled:opacity-70 disabled:cursor-not-allowed flex justify-center items-center"
          >
            {loading ? (
              <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            ) : 'Entrar'}
          </button>
        </form>

        <p className="text-center text-sm text-slate-600 mt-8">
          ¿No tienes una cuenta? <Link href="/registro" className="text-teal-600 font-medium hover:text-teal-700">Regístrate</Link>
        </p>
      </div>
    </div>
  )
}
