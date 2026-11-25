import Link from 'next/link'
import { ArrowRight, Send, Landmark, RotateCcw } from 'lucide-react'
import BrandLogo from '@/components/BrandLogo'

export default function Home() {
  return (
    <main className="caleta-home">
      <div className="home-notice">Hecha con ganas. Pensada para ti.</div>
      <header className="home-header">
        <BrandLogo />
        <nav aria-label="Cuenta" className="home-nav"><Link href="/login">Iniciar sesión</Link><Link href="/registro" className="home-register">Crear cuenta</Link></nav>
      </header>
      <section className="home-hero" aria-labelledby="home-title">
        <div>
          <p className="home-eyebrow">De Ecuador, con ideas grandes.</p>
          <h1 id="home-title">Tu mundo.<br /><span>Tu plata.</span><br />Tu Caleta.</h1>
          <p className="home-intro">Una caleta para tus ideas, tus planes y todo lo que viene. Estamos construyendo una forma más cercana de conectar tu trabajo con el mundo.</p>
          <div className="home-cta"><Link href="/login" className="home-primary">Iniciar sesión <ArrowRight size={19} aria-hidden="true" /></Link><a href="#demo-testeo" className="home-text-link">¿Primera vez? Explora la demo</a></div>
        </div>
        <div className="home-art" aria-label="La casa de Caleta">
          <span className="home-art-label">Tu lugar para lo que viene.</span>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/brand/caleta-casa.png" width="1297" height="1200" alt="La casa que forma la última a de Caleta" />
          <span className="home-art-sign">Ideas grandes. Pasos claros.</span>
        </div>
      </section>
      <section id="demo-testeo" className="home-demo" aria-labelledby="demo-title">
        <div className="home-demo-intro">
          <div><p className="home-eyebrow">Cuenta de práctica</p><h2 id="demo-title">Entra, prueba y cuéntanos.</h2><p>Empieza con USD 1.000,00 ficticios. Simula un envío, prueba un retiro y descubre cómo se siente usar Caleta.</p><p className="home-small">Sin registro. Sin dinero real. En la exploración libre puedes reiniciar cuando quieras.</p></div>
          <a className="home-primary" href="/demo">Entrar a la demo <ArrowRight size={19} aria-hidden="true" /></a>
        </div>
        <div className="home-features">
          {[{ icon: Send, title: 'Envía con claridad', text: 'Elige un contacto de prueba y revisa los datos antes de confirmar.' }, { icon: Landmark, title: 'Prueba un retiro', text: 'Usa una cuenta bancaria ficticia y consulta el comprobante.' }, { icon: RotateCcw, title: 'Explora a tu ritmo', text: 'Revisa tus movimientos. Todo ocurre con dinero de práctica.' }].map(({ icon: Icon, title, text }) => (
            <article key={title}><Icon size={28} aria-hidden="true" /><h3>{title}</h3><p>{text}</p></article>
          ))}
        </div>
        <p className="home-study">¿Te invitó el equipo a una prueba? <a href="/demo?estudio=1">Participar en una sesión guiada</a></p>
      </section>
      <footer className="home-footer"><BrandLogo /><p>Demo académica. Sin conexión con bancos ni pagos reales.</p><a href="/test-usabilidad.html">Panel del moderador</a></footer>
    </main>
  )
}
