'use client'

import { useState } from 'react'
import Link from 'next/link'
import { resetPassword } from './actions'
import { KeyRound, Lock, Eye, EyeOff, ArrowLeft } from 'lucide-react'

export default function ResetPasswordPage() {
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [showPassword, setShowPassword] = useState(false)
  const [showConfirmPassword, setShowConfirmPassword] = useState(false)

  async function handleSubmit(formData: FormData) {
    const password = formData.get('password') as string
    const confirmPassword = formData.get('confirm_password') as string

    if (!password || password.length < 6) {
      setError('La contraseña debe tener al menos 6 caracteres.')
      return
    }

    if (password !== confirmPassword) {
      setError('Las contraseñas no coinciden. Por favor verifica ambos campos.')
      return
    }

    setLoading(true)
    setError('')

    const res = await resetPassword(formData)
    if (res?.error) {
      setError(res.error)
      setLoading(false)
    }
  }

  return (
    <div className="flex-1 flex flex-col justify-center items-center p-4 sm:p-6 min-h-[calc(100vh-4rem)]">
      <div className="w-full max-w-md bg-white p-6 sm:p-8 rounded-2xl shadow-sm border border-slate-200/80">
        
        {/* Cabecera con Logo e Icono */}
        <div className="text-center mb-6">
          <Link 
            href="/" 
            className="inline-block text-2xl font-bold text-slate-900 tracking-tight mb-4 hover:opacity-90 transition-opacity"
          >
            Caleta<span className="text-teal-600">.</span>
          </Link>

          <div className="w-12 h-12 bg-teal-50 text-teal-600 rounded-2xl flex items-center justify-center mx-auto mb-3 border border-teal-100/80 shadow-xs">
            <KeyRound className="w-6 h-6 text-teal-600" />
          </div>

          <h1 className="text-xl font-semibold text-slate-900 tracking-tight">
            Restablecer contraseña
          </h1>
          <p className="text-slate-500 text-sm mt-1.5">
            Crea una nueva contraseña segura para acceder a tu cuenta.
          </p>
        </div>

        {/* Formulario */}
        <form action={handleSubmit} className="space-y-4">
          
          {/* Campo: Nueva Contraseña */}
          <div>
            <label className="block text-xs font-medium text-slate-700 uppercase tracking-wider mb-1.5" htmlFor="password">
              Nueva contraseña
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
              <input
                id="password"
                name="password"
                type={showPassword ? 'text' : 'password'}
                required
                minLength={6}
                className="w-full pl-10 pr-11 py-2.5 bg-slate-50/50 border border-slate-300/80 rounded-xl focus:bg-white focus:ring-2 focus:ring-teal-500/20 focus:border-teal-600 transition-all outline-none text-sm text-slate-800 placeholder:text-slate-400"
                placeholder="Mínimo 6 caracteres"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                tabIndex={-1}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1 rounded-lg transition-colors"
                aria-label={showPassword ? 'Ocultar contraseña' : 'Ver contraseña'}
              >
                {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
            </div>
          </div>

          {/* Campo: Confirmar Contraseña */}
          <div>
            <label className="block text-xs font-medium text-slate-700 uppercase tracking-wider mb-1.5" htmlFor="confirm_password">
              Confirmar contraseña
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
              <input
                id="confirm_password"
                name="confirm_password"
                type={showConfirmPassword ? 'text' : 'password'}
                required
                minLength={6}
                className="w-full pl-10 pr-11 py-2.5 bg-slate-50/50 border border-slate-300/80 rounded-xl focus:bg-white focus:ring-2 focus:ring-teal-500/20 focus:border-teal-600 transition-all outline-none text-sm text-slate-800 placeholder:text-slate-400"
                placeholder="Repite tu contraseña"
              />
              <button
                type="button"
                onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                tabIndex={-1}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1 rounded-lg transition-colors"
                aria-label={showConfirmPassword ? 'Ocultar contraseña' : 'Ver contraseña'}
              >
                {showConfirmPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
            </div>
          </div>

          {/* Mensaje de Error */}
          {error && (
            <div className="bg-red-50 text-red-600 text-xs sm:text-sm p-3 rounded-xl border border-red-200/70 flex items-start gap-2 animate-in fade-in duration-200">
              <span className="font-medium">•</span>
              <span>{error}</span>
            </div>
          )}

          {/* Botón Principal */}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-teal-600 text-white font-medium py-2.5 px-4 rounded-xl hover:bg-teal-700 active:scale-[0.99] transition-all duration-150 disabled:opacity-70 disabled:cursor-not-allowed flex justify-center items-center gap-2 shadow-xs mt-2"
          >
            {loading ? (
              <>
                <svg className="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>Guardando cambios...</span>
              </>
            ) : (
              'Actualizar contraseña'
            )}
          </button>
        </form>

        {/* Enlace inferior de regreso */}
        <div className="text-center mt-6 pt-5 border-t border-slate-100">
          <Link 
            href="/login" 
            className="inline-flex items-center gap-1.5 text-sm font-medium text-slate-600 hover:text-teal-600 transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Volver a iniciar sesión</span>
          </Link>
        </div>

      </div>
    </div>
  )
}
