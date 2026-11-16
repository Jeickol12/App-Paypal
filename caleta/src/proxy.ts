import { NextResponse, type NextRequest } from 'next/server'
import { updateSession } from '@/utils/supabase/middleware'

export async function proxy(request: NextRequest) {
  // The practice account is fully local and never uses real authentication or funds.
  if (request.nextUrl.pathname === '/demo' || request.nextUrl.pathname === '/demo/') {
    return NextResponse.rewrite(new URL('/demo.html', request.url))
  }
  if (request.nextUrl.pathname === '/demo.html') {
    return NextResponse.next()
  }
  return await updateSession(request)
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * Feel free to modify this pattern to include more paths.
     */
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ],
}
