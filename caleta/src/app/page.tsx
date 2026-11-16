import Link from "next/link";
import { ArrowRight, House, Send, Landmark, RotateCcw } from "lucide-react";

export default function Home() {
  return (
    <main className="min-h-screen bg-[#f8f5ed] text-[#203f3b]">
      <div className="bg-[#284f48] px-4 py-2 text-center text-[11px] text-[#f9f5e9]">Caleta · Tu dinero, en casa.</div>
      <header className="mx-auto flex max-w-6xl items-center justify-between border-b border-[#dedfd2] px-6 py-6">
        <Link href="/" aria-label="Caleta, inicio" className="flex items-center gap-2 text-3xl font-bold tracking-tighter"><House className="size-8 text-[#ac593c]" aria-hidden="true" />caleta<span className="text-[#ac593c]">.</span></Link>
        <nav aria-label="Cuenta" className="flex items-center gap-5 text-xs font-medium"><Link href="/login" className="rounded p-2 hover:underline">Iniciar sesión</Link><Link href="/registro" className="hidden rounded-lg border border-[#d2d9ca] px-4 py-3 sm:block">Crear cuenta</Link></nav>
      </header>
      <section className="mx-auto grid max-w-6xl items-center gap-10 px-6 py-12 md:grid-cols-2 md:py-20">
        <div>
          <p className="mb-6 text-[10px] font-semibold uppercase tracking-[0.2em] text-[#64736c]">De aquí. Para llegar más lejos.</p>
          <h1 className="text-5xl leading-[1.08] font-medium tracking-[-0.045em] sm:text-6xl">Tu mundo crece.<br />Tu dinero,<br /><span className="text-[#a95a3c]">en casa.</span></h1>
          <p className="mt-7 max-w-md text-base leading-7 text-[#62756a]">Una caleta para lo que te mueve. Estamos construyendo una forma más cercana de conectar tu trabajo con el mundo, desde Ecuador.</p>
          <Link href="/login" className="mt-8 inline-flex items-center gap-6 rounded-xl bg-[#214e47] px-6 py-4 text-sm font-medium text-white hover:bg-[#133b35] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#ac593c]">Iniciar sesión <ArrowRight className="size-4" aria-hidden="true" /></Link>
          <p className="mt-4 text-xs text-[#65776a]">¿Todavía no tienes cuenta? <Link href="/registro" className="font-semibold underline underline-offset-4">Crea tu cuenta</Link></p>
        </div>
        <div className="overflow-hidden rounded-[28px] border border-[#dde1ce] bg-[#e8eadb]">
          <div className="flex items-center gap-2 px-7 pt-7 text-[10px] tracking-widest text-[#516c5f]"><House className="size-4" aria-hidden="true" /> CERCA DE LO TUYO</div>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/caleta-landscape.svg" alt="Ilustración de una casa entre montañas, agua y un sol cálido" width="600" height="390" className="w-full" />
          <p className="px-7 pb-7 text-sm text-[#365b4b]">Raíces ecuatorianas. Mirada al mundo.</p>
        </div>
      </section>
      <section id="demo-testeo" aria-labelledby="demo-title" className="mx-auto max-w-6xl px-6 pb-14">
        <div className="rounded-[28px] border border-[#dde1ce] bg-[#ecefdf] p-6 sm:p-10">
          <div className="flex flex-col justify-between gap-6 md:flex-row md:items-center">
            <div className="max-w-xl">
              <p className="mb-3 text-[10px] font-semibold uppercase tracking-[0.2em] text-[#64736c]">Espacio de pruebas · Demo de usabilidad</p>
              <h2 id="demo-title" className="text-3xl font-medium tracking-tight">Prueba Caleta. Ayúdanos a mejorar.</h2>
              <p className="mt-4 text-sm leading-7 text-[#62756a]">Explora la experiencia con una cuenta de prueba y USD 1.000 ficticios. Simula movimientos y descubre cómo se siente usar Caleta.</p>
              <p className="mt-3 text-xs text-[#65776a]">Sin registro. Sin dinero real. Puedes reiniciar cuando quieras.</p>
              <p className="mt-3 text-xs text-[#65776a]">¿Te invitó el equipo a una prueba? <a href="/demo?estudio=1" className="font-semibold underline underline-offset-4">Participar en una sesión guiada</a></p>
            </div>
            <a href="/demo" className="inline-flex shrink-0 items-center justify-center gap-4 self-start rounded-xl border border-[#214e47] bg-[#fffdf8] px-6 py-4 text-sm font-semibold text-[#214e47] hover:bg-[#e2e8d4] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#ac593c] md:self-auto">Entrar a la demo <ArrowRight className="size-4" aria-hidden="true" /></a>
          </div>
          <div className="mt-8 grid gap-4 sm:grid-cols-3">
        {[{ icon: Send, title: "Mueve tu dinero", text: "Simula un envío a tus contactos y revisa los datos antes de confirmar." }, { icon: Landmark, title: "Un paso más cerca", text: "Prueba un retiro a una cuenta bancaria ficticia y consulta el comprobante." }, { icon: RotateCcw, title: "Explora a tu ritmo", text: "Revisa tus movimientos y reinicia tu saldo cuando quieras volver a empezar." }].map(({ icon: Icon, title, text }) => (
          <article key={title} className="rounded-2xl border border-[#e2e5d7] bg-[#fffdf8] p-6"><Icon className="mb-5 size-6 text-[#a96947]" aria-hidden="true" /><h3 className="text-base font-semibold">{title}</h3><p className="mt-3 text-xs leading-6 text-[#62756a]">{text}</p></article>
        ))}
          </div>
        </div>
      </section>
      <footer className="mx-auto flex max-w-6xl flex-wrap justify-between gap-4 border-t border-[#dedfd2] px-6 py-6 text-[10px] text-[#637468]"><span>Caleta · Tu dinero, en casa.</span><span>Demo académica. Sin conexión con bancos ni pagos reales.</span></footer>
    </main>
  );
}
