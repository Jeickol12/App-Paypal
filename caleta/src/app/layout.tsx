import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Caleta - Cobra globalmente. Recibe localmente.",
  description: "Plataforma para freelancers y PYMEs de Ecuador para cobrar a clientes internacionales.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className={`${inter.className} bg-slate-50 text-slate-800 min-h-screen flex flex-col`} suppressHydrationWarning>
        {children}
      </body>
    </html>
  );
}
