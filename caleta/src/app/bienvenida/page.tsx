import { createClient } from '@/utils/supabase/server'
import { redirect } from 'next/navigation'
import { logout } from '@/app/login/actions'
import { LogOut, CheckCircle, AlertCircle, Clock } from 'lucide-react'

export const instant = false;

export default async function WelcomePage() {
  const supabase = await createClient()

  const { data: { user }, error } = await supabase.auth.getUser()

  if (error || !user) {
    redirect('/login')
  }

  const isEmailConfirmed = !!user.email_confirmed_at
  const accountType = user.user_metadata?.account_type === 'business' ? 'Empresa' : 'Freelancer'
  const fullName = user.user_metadata?.full_name || 'Usuario'

  return (
    <div className="flex-1 bg-slate-50 min-h-screen">
      <header className="bg-white border-b border-slate-200">
        <div className="max-w-5xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="text-xl font-bold text-slate-900">
            Caleta <span className="text-teal-600">.</span>
          </div>
          <form action={logout}>
            <button type="submit" className="text-slate-600 hover:text-slate-900 font-medium flex items-center gap-2">
              <LogOut className="w-4 h-4" />
              Cerrar Sesión
            </button>
          </form>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-12">
        <div className="mb-10">
          <h1 className="text-3xl font-bold text-slate-900 mb-2">¡Hola, {fullName}! 👋</h1>
          <p className="text-slate-600 text-lg">Bienvenido a tu panel de control de NexoCobro.</p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          <div className="md:col-span-2 space-y-6">
            <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
              <h2 className="text-lg font-bold text-slate-900 mb-4 border-b border-slate-100 pb-4">Estado de tu cuenta</h2>
              
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  {isEmailConfirmed ? (
                    <CheckCircle className="w-6 h-6 text-teal-600 shrink-0" />
                  ) : (
                    <AlertCircle className="w-6 h-6 text-amber-500 shrink-0" />
                  )}
                  <div>
                    <p className="font-medium text-slate-900">Correo electrónico</p>
                    <p className="text-sm text-slate-600">
                      {isEmailConfirmed ? 'Tu correo electrónico ha sido verificado correctamente.' : 'Revisa tu bandeja de entrada para verificar tu correo.'}
                    </p>
                  </div>
                </li>
                
                <li className="flex items-start gap-3 opacity-60">
                  <Clock className="w-6 h-6 text-slate-400 shrink-0" />
                  <div>
                    <p className="font-medium text-slate-900">Verificación de Identidad (KYC/KYB)</p>
                    <p className="text-sm text-slate-600">Próximo paso: Sube tus documentos para operar. (Sprint 2)</p>
                  </div>
                </li>

                <li className="flex items-start gap-3 opacity-60">
                  <Clock className="w-6 h-6 text-slate-400 shrink-0" />
                  <div>
                    <p className="font-medium text-slate-900">Cuenta Bancaria en Ecuador</p>
                    <p className="text-sm text-slate-600">Configura tu cuenta bancaria local para recibir fondos. (Sprint 3)</p>
                  </div>
                </li>
              </ul>
            </div>

            <div className="bg-gradient-to-r from-teal-600 to-cyan-700 rounded-2xl p-6 shadow-sm text-white">
              <h2 className="text-lg font-bold mb-2">Próximamente: Links de Pago</h2>
              <p className="text-teal-50 mb-4">
                Muy pronto podrás generar links de cobro para enviar a tus clientes internacionales y recibir el dinero directo en tu cuenta local en Ecuador.
              </p>
              <button disabled className="bg-white/20 text-white px-4 py-2 rounded-lg font-medium cursor-not-allowed">
                Crear nuevo link (Próximamente)
              </button>
            </div>
          </div>

          <div className="space-y-6">
            <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm">
              <h2 className="text-sm font-bold text-slate-400 uppercase tracking-wider mb-4">Perfil</h2>
              <div className="space-y-3">
                <div>
                  <p className="text-xs text-slate-500">Nombre / Razón Social</p>
                  <p className="font-medium text-slate-900">{fullName}</p>
                </div>
                <div>
                  <p className="text-xs text-slate-500">Correo</p>
                  <p className="font-medium text-slate-900">{user.email}</p>
                </div>
                <div>
                  <p className="text-xs text-slate-500">Tipo de cuenta</p>
                  <p className="font-medium text-slate-900">
                    <span className="inline-block bg-slate-100 text-slate-700 px-2 py-1 rounded text-sm mt-1">
                      {accountType}
                    </span>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
