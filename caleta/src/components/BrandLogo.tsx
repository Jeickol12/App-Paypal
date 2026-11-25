import Link from 'next/link'

export default function BrandLogo({ className = '' }: { className?: string }) {
  return (
    <Link href="/" className={`caleta-brand-link ${className}`} aria-label="Caleta, inicio">
      {/* Use the approved artwork rather than rebuilding the lettering with a font. */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src="/brand/caleta-logo.png" alt="Caleta" width="2166" height="726" className="caleta-logo" />
    </Link>
  )
}
