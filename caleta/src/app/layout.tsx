import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Caleta · Tu mundo. Tu plata. Tu Caleta.",
  description: "Una caleta para tus ideas y tus planes. Explora nuestra cuenta de práctica con dinero ficticio, desde Ecuador.",
  icons: { icon: '/brand/caleta-casa.png', apple: '/brand/caleta-casa.png' },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className="min-h-screen flex flex-col" suppressHydrationWarning>
        {children}
      </body>
    </html>
  );
}
