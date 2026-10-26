import Link from "next/link";
import { ArrowRight, Globe, Wallet } from "lucide-react";

export default function Home() {
  return (
    <main className="flex-1 flex flex-col items-center justify-center p-6 sm:p-24 bg-gradient-to-br from-slate-50 to-slate-100">
      <div className="w-full max-w-4xl flex justify-between items-center py-6 absolute top-0 px-6 sm:px-24">
        <h1 className="text-2xl font-bold text-slate-900 flex items-center gap-2">
          Caleta <span className="text-teal-600">.</span>
        </h1>
        <div className="flex gap-4">
          <Link href="/login" className="text-slate-600 font-medium hover:text-slate-900 px-4 py-2 transition-colors">
            Iniciar Sesión
          </Link>
          <Link href="/registro" className="bg-teal-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-teal-700 transition-colors hidden sm:block">
            Registrarse
          </Link>
        </div>
      </div>

      <div className="text-center max-w-3xl mt-16">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal-100 text-teal-800 text-sm font-medium mb-6">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-teal-500"></span>
          </span>
          Disponible para Ecuador
        </div>
        <h2 className="text-5xl sm:text-7xl font-extrabold text-slate-900 tracking-tight leading-tight mb-8">
          Cobra <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-cyan-600">globalmente.</span><br />
          Recibe <span className="text-slate-900">localmente.</span>
        </h2>
        <p className="text-xl text-slate-600 mb-12 max-w-2xl mx-auto">
          La plataforma definitiva para freelancers y PYMEs ecuatorianas. Recibe pagos internacionales con tarjeta y obtén tus dólares directo en tu banco local.
        </p>
        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <Link href="/registro" className="bg-slate-900 text-white px-8 py-4 rounded-xl font-medium hover:bg-slate-800 transition-all flex items-center justify-center gap-2 shadow-lg shadow-slate-900/20 group">
            Comenzar ahora
            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </Link>
          <Link href="/login" className="bg-white text-slate-900 border border-slate-200 px-8 py-4 rounded-xl font-medium hover:bg-slate-50 transition-colors flex items-center justify-center sm:hidden">
            Iniciar Sesión
          </Link>
        </div>
      </div>

      <div className="grid sm:grid-cols-2 gap-8 mt-24 max-w-4xl w-full">
        <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
          <div className="w-12 h-12 bg-teal-100 text-teal-600 rounded-xl flex items-center justify-center mb-6">
            <Globe className="w-6 h-6" />
          </div>
          <h3 className="text-xl font-bold text-slate-900 mb-3">Links de pago globales</h3>
          <p className="text-slate-600">Envía links de cobro profesionales a tus clientes en EE.UU., Europa o cualquier parte del mundo. Sin necesidad de que ellos creen cuentas.</p>
        </div>
        <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100">
          <div className="w-12 h-12 bg-blue-100 text-blue-600 rounded-xl flex items-center justify-center mb-6">
            <Wallet className="w-6 h-6" />
          </div>
          <h3 className="text-xl font-bold text-slate-900 mb-3">A tu cuenta en Ecuador</h3>
          <p className="text-slate-600">Tu dinero se acredita directamente en tu cuenta de banco local de forma rápida, segura y transparente, con comisiones justas.</p>
        </div>
      </div>
    </main>
  );
}
