# Memoria del Proyecto: Caleta - Plataforma de Cobros Internacionales

**Fecha de última actualización:** 26 de Octubre de 2026  
**Ubicación del Proyecto:** `C:\Users\jeick\OneDrive\Desktop\App Paypal\caleta`  
**Institución:** Universidad de Especialidades Espíritu Santo (UEES)  
**Docente Titular:** Marco Vinicio Sotomayor Sánchez  

Esta memoria detalla el estado exacto del proyecto, su código, arquitectura, planificación Scrum y entregables académicos generados para retomar el trabajo de inmediato en futuras sesiones.

---

## 1. Organización Oficial del Scrum Team

- **Product Owner:** Emilio Zúñiga (Aceptación de incrementos, modelo de negocio, cumplimiento y proveedores).
- **Scrum Master:** Romina Sigcho (UX/UI, aseguramiento de calidad, documentación y facilitación ágil).
- **Desarrollador Backend & Pagos:** Jeickol Moreira (Arquitectura de datos, Supabase Auth SSR, PostgreSQL RLS y pagos).
- **Desarrollador Frontend & DevOps:** Cristhian Grunauer (Next.js 16, Tailwind CSS v4, Vercel y pipeline GitHub Actions).

---

## 2. Entregables Formales Generados (Primer Avance - Sprint 1)

En la carpeta raíz del proyecto `entregables/` se encuentran compilados y verificados:

1. **`entregables/Informe_Primer_Avance_Sprint_1.docx`** (1.0 MB):
   - Documento editable de 33 páginas en formato Word formal.
   - Incluye carátula académica sobria UEES, índices jerárquicos (general, tablas, figuras), 11 secciones analíticas, referencias en APA 7 y 3 anexos.
2. **`entregables/Informe_Primer_Avance_Sprint_1.pdf`** (899 KB):
   - Copia oficial compilada vía Word Automation.
   - Contiene 9 tablas técnicas, 5 figuras en alta resolución y metadatos limpios bajo la autoría de *"Universidad Espíritu Santo - Scrum Team Caleta"*.
3. **`entregables/Presentacion_Primer_Avance_Sprint_1.pdf`** (620 KB):
   - Presentación ejecutiva oficial de 8 diapositivas estilo Keynote en formato 16:9 widescreen para la materia *Herramientas Ágiles para Reuniones*.
   - Incluye roles específicos de cada integrante, mockups de navegador con capturas del software real, métricas del Burndown Chart y marco Scrum del Sprint 1.
4. **`entregables/Presentacion_Primer_Avance_Sprint_1.pptx`** (977 KB):
   - Versión editable de la presentación generada mediante `python-pptx` y automatización COM.
5. **Recursos Gráficos y Scripts Generados (`assets/` y scripts raíz):**
   - `generar_presentacion_sprint1.py`: Script generador de las 8 diapositivas y exportación COM a PDF.
   - `assets/burndown_sprint1.png`: Burndown Chart con línea ideal (60 h a 0 h) y línea real registrada hasta el Día 7 (18 h restantes).
   - `assets/diagrama_arquitectura.png`: Diagrama de arquitectura desacoplada (Next.js 16 + Supabase SSR).
   - `assets/diagrama_flujo_fondos.png`: Mapeo conceptual de fondos y liquidación local.
   - `assets/pantalla_landing.png` y `assets/pantalla_registro.png`: Evidencias visuales de la interfaz en funcionamiento.

---

## 3. Estado Técnico del Incremento de Software (`caleta/`)

Se implementó y verificó el incremento del Sprint 1 (PB-01 a PB-04):

- **Stack Tecnológico:**
  - Next.js 16.4.0 (App Router, Server Components, Turbopack).
  - React 19.3.0 y React DOM 19.3.0.
  - Tailwind CSS v4.3.3 (utilizando `@import "tailwindcss";`).
  - Supabase SSR v0.12.7 y Supabase JS v2.117.3.
  - TypeScript 5, ESLint 9 y Lucide React v1.52.0.
- **Rutas e Interfaces Implementadas (`src/app/`):**
  - `/`: Landing page institucional con propuesta de valor (*"Cobra globalmente. Recibe localmente"*).
  - `/registro`: Formulario tipificado que diferencia entre **Freelancer / Profesional** y **Empresa / PYME**.
  - `/login`: Formulario de inicio de sesión seguro con manejo visual de errores y estados de carga.
  - `/recuperar` y `/reset-password`: Flujo completo de solicitud y restablecimiento de contraseña vía token.
  - `/bienvenida`: Dashboard protegido accesible únicamente con sesión activa.
  - `/auth/callback`: Route Handler para manejo de sesiones PKCE.
- **Seguridad y Base de Datos:**
  - `src/proxy.ts`: Middleware de protección de rutas privadas (redirección a `/login` si no hay sesión).
  - `supabase/migrations/20261012000000_initial_schema.sql`: Tabla `public.profiles` vinculada a `auth.users`, función y trigger atómico `handle_new_user()`, y políticas de Row Level Security (RLS) que aíslan la información entre usuarios.
  - `.github/workflows/ci.yml`: Pipeline de CI automatizado (Type-checking con `tsc`, Linting con ESLint y Build de producción).

---

## 4. Planificación del MVP (Consolidada a 4 Sprints de 2 semanas)

- **Sprint 1 (12/10/2026 – 23/10/2026):** *Fundamentos e Incremento Base* (PB-01 a PB-04). **[En curso / Cierre]**
  - Esfuerzo planificado: 60 horas.
  - Horas restantes registradas al Día 7 (20/10/2026): 18 horas.
- **Sprint 2 (26/10/2026 – 06/11/2026):** *Onboarding y Activación* (PB-05 a PB-07).
  - Carga y almacenamiento encriptado de documentos KYC/KYB en Supabase Storage.
  - CRUD para registro y validación de cuentas bancarias ecuatorianas en USD.
  - Generador de enlaces de pago (Payment Links) con montos y expiración.
- **Sprint 3 (09/11/2026 – 20/11/2026):** *Cobro Internacional y Ledger* (PB-08 a PB-10).
  - Integración de pasarela internacional (Stripe Connect sandbox).
  - Procesamiento de pagos con tarjeta de crédito/débito y webhooks con idempotencia.
  - Registro de comisiones (2.9%+0.30 pasarela, 2.1% Caleta) y ledger contable de saldos.
- **Sprint 4 (23/11/2026 – 04/12/2026):** *Liquidación Local y Piloto* (PB-11 a PB-18).
  - Módulo de retiros a cuentas locales vía SPI / transferencias en Ecuador ($3.00 fijo).
  - Dashboard transaccional, suite de pruebas end-to-end y piloto con 5 a 10 freelancers reales.

---

## 5. Auditoría de Seguridad y Privacidad

- Se auditó que los documentos de entrega **no contienen rutas locales privadas** (`C:\Users\...`), nombres de usuario de Windows, ni secretos en texto plano.
- Las variables de entorno de desarrollo en `.env.local` y `.env.example` mantienen valores temporales seguros (`https://dummy.supabase.co`).
- Los metadatos de autoría del DOCX y PDF están asignados formalmente a *"Universidad Espíritu Santo - Scrum Team Caleta"*.

---

## 6. Próximos Pasos Inmediatos para Retomar

1. **Cierre Formal del Sprint 1 (al 23 de octubre):**
   - Crear el proyecto en Supabase real y aplicar la migración `initial_schema.sql`.
   - Probar el despacho de correos SMTP de activación y recuperación de contraseña.
   - Completar las horas de los días 8, 9 y 10 en la Tabla 7 del informe (meta: 0 horas).
   - Realizar la reunión de Sprint Review y Sprint Retrospective con el equipo.
2. **Arranque del Sprint 2 (26 de octubre):**
   - Configurar los buckets privados en Supabase Storage con políticas RLS para cédulas y RUC.
   - Construir la interfaz de subida documental de KYC/KYB.
   - Desarrollar la tabla y vistas de cuentas bancarias locales ecuatorianas.
