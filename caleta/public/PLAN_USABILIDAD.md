# Caleta · Usability Test Plan UTP-1.0

Protocolo original: 16 de noviembre de 2026. Actualización de estado: 25 de noviembre de 2026. El equipo entregó cinco registros principales y un piloto de sesiones del 16 y 23 de noviembre, conservados fuera del repositorio público. Este plan usa prácticas de planificación de NN/g y GOV.UK. No afirma certificación ISO, conformidad legal ni cumplimiento de una rúbrica académica no entregada.

La identidad caleta-brand-1.0-2026-11-25 es posterior a esas sesiones. Las tareas y límites se mantienen; las nuevas sesiones deben analizarse como otra ronda. El panel añade la versión a las exportaciones futuras. No atribuir resultados históricos a este rediseño.

## 1. Propósito y preguntas

Estudio formativo: encontrar dificultades del prototipo e incorporarlas al backlog antes de desarrollar pagos reales.

- Comprensión: ¿se distingue saldo disponible de dinero real? ¿se reconocen destinatarios y movimientos?
- Eficacia y control: ¿se completan un envío y un retiro al destino correcto? ¿se puede desistir antes de confirmar?
- Recuperación: ¿se entiende el mensaje ante saldo insuficiente y se decide un siguiente paso?

No se evalúan registro, autenticación, KYC, cobros internacionales, integraciones bancarias, seguridad financiera ni éxito comercial. La identidad de marca puede discutirse en el cierre, pero una opinión no demuestra usabilidad.

## 2. Método, equipo y muestra

Sesiones individuales moderadas de 20–25 minutos, con pensamiento en voz alta. Un moderador facilita; un observador toma notas sin intervenir (si está disponible). Identificar a ambos y dar un contacto del equipo antes del consentimiento. Compartir únicamente la demo al participante; mantener el panel de moderación en otro dispositivo o pantalla no compartida.

Reclutamiento propuesto: cinco adultos freelancers/profesionales independientes de Ecuador, usuarios actuales o potenciales de transferencias digitales, con experiencia variada. No incluir al equipo desarrollador como muestra principal. Un piloto adicional ajeno al desarrollo prueba el guion, los tiempos y la exportación; no incluirlo en el resumen principal. Si solo hay compañeros disponibles, declararlo como muestra por conveniencia. Si se incluye PYME, analizarla por separado y no asumir que cinco participantes cubren ambos segmentos.

Coordinar necesidades de accesibilidad y dispositivo habitual. Registrar móvil/escritorio, navegador y versión del prototipo. No hacer afirmaciones comparativas móvil/escritorio con uno o dos casos por grupo. No cambiar la interfaz entre participantes de la misma ronda; si se corrige un bloqueo, registrar nueva versión y separar las sesiones.

## 3. Entorno y preparación

- Participante: https://app-paypal-pied.vercel.app/demo?estudio=1
- Moderador: https://app-paypal-pied.vercel.app/test-usabilidad.html
- Exploración libre fuera del estudio: https://app-paypal-pied.vercel.app/demo

El modo estudio usa saldo en memoria: cada carga empieza con USD 1.000 y un solo movimiento inicial, sin reutilizar ni cambiar los movimientos guardados por la demo libre. La aceptación habilita la bienvenida; no lleva directamente al panel. No hay pistas de tareas, criterios, cronómetro ni puntuaciones en la pantalla del participante. Los avisos de dinero ficticio son parte del producto y deben mantenerse.

Se preparan seis accesos independientes con `&participante=P01`, `P02`, `P03`, `P04`, `P05` y `P06`. Los dos accesos adicionales son `/demo?estudio=1&participante=P05` y `/demo?estudio=1&participante=P06`, disponibles en el panel del moderador. Cada pestaña tiene su propio saldo, incluso si dos personas abren el mismo código; no existe un saldo compartido en servidor. El código es una etiqueta de investigación, no una credencial ni una cuenta autenticada. Todos usan el mismo perfil ficticio Alex para mantener iguales los escenarios. Cada moderador debe usar una ficha independiente con el código correspondiente. Probar simultáneamente requiere observación separada por persona; si solo hay un moderador, realizar las sesiones por turnos. La aplicación no registra automáticamente resultados ni sincroniza transacciones entre dispositivos. Tener seis accesos disponibles no equivale a seis participantes reclutados o sesiones completadas.

La recarga reinicia saldo y aceptación: si ocurre durante una tarea, registrarla como interrupción técnica y restaurar el escenario fuera de la vista del participante. No iniciar dos sesiones en una misma pestaña. Antes de cada persona, exportar/verificar el registro del moderador y usar «Preparar otro participante»; abrir el enlace de estudio de nuevo. No hay sincronización automática entre las dos pantallas.

## 4. Información, aceptación y retiro

El equipo académico Caleta explica quién modera y observa, su contacto, propósito, duración, datos recogidos, destino académico (equipo y docente) y carácter voluntario. Permitir preguntas y adaptaciones. La persona puede omitir tareas o retirarse sin consecuencias. Solo adultos en esta ronda.

Modo por defecto: notas con código P01–P999; sin nombres, correos ni cuentas reales de participantes. Se registran acciones, tiempos, errores, ayudas, valoraciones y citas breves sin identificación. La pantalla requiere aceptación no premarcada; el moderador registra la aceptación y la hora después de observarla. No es una firma digital ni evidencia de identidad. Si no acepta, no crear un registro de sesión.

No se graba audio, vídeo ni pantalla desde la herramienta. Si el equipo quiere grabar con otro programa, debe explicar uso, acceso, conservación y retiro, y obtener autorización separada antes de hacerlo; esta versión del plan/panel supone que no hay grabaciones.

Los movimientos de estudio se descartan al terminar/recargar. Las notas están solo en memoria del panel hasta su exportación; no se suben a una base de datos. El hosting puede conservar registros técnicos de acceso. El equipo guarda los JSON en una carpeta restringida y elimina registros individuales a los 30 días de cada sesión. Esa eliminación de archivos exportados es manual, responsabilidad del equipo; la app no puede garantizarla. Para retiro, la persona comunica su código al contacto entregado: descartar el panel y eliminar exportaciones/notas correspondientes. No publicar archivos individuales; presentar únicamente hallazgos sin identificación.

## 5. Guion y agenda

1. Presentación, información y aceptación: 3 minutos.
2. Contexto breve: perfil y experiencia en transferencias, sin preguntas sensibles: 2 minutos.
3. Seis tareas: aproximadamente 12–15 minutos.
4. Preguntas de cierre: 3–5 minutos.

Leer: «Evaluamos la interfaz, no a ti. Puedes detenerte u omitir preguntas. Cuéntame lo que piensas. Primero intenta resolverlo a tu manera; no hay problema si no logras una tarea».

Presentar una tarea a la vez. No mostrar botones, rutas, criterios ni saldos finales. Si pregunta cómo proceder: «¿Qué harías si estuvieras usando esto por tu cuenta?». No elogiar decisiones durante la ejecución. Si hay un bloqueo, observar primero; luego ayudar solo si lo solicita o se llega al límite, registrando la ayuda. Detener inmediatamente si la persona desea abandonar. Cada tarea tiene límite operativo; no presentarlo como examen o cuenta regresiva.

## 6. Escenarios y criterios (solo equipo)

| Tarea | Escenario leído al participante | Estado inicial | Éxito observable | Límite |
|---|---|---|---|---|
| T1 | Es la primera vez que pruebas Caleta. Explora esta cuenta de práctica y cuéntame cuánto dinero tienes disponible y si es dinero real. | Bienvenida aceptada; USD 1.000 | Accede al panel y reconoce saldo y carácter ficticio | 120 s |
| T2 | Sofía Torres terminó un trabajo de diseño para ti. Le debes USD 150. Resuelve ese pago con tu cuenta de práctica. | Panel; USD 1.000 | Un envío a Sofía de 150 confirmado; saldo 850 | 180 s |
| T3 | Necesitas disponer de USD 200 en la cuenta bancaria de prueba de Alex. Usa Caleta para dejarlo resuelto. | USD 850; envío de 150 | Un retiro de 200; saldo 650 | 180 s |
| T4 | Antes de seguir, quieres comprobar qué pasó con tu dinero. Cuéntame cuáles fueron tus dos últimas operaciones y cuánto puedes usar ahora. | USD 650; envío 150 y retiro 200 | Identifica operaciones/importes y saldo 650 | 120 s |
| T5 | Ahora tienes que pagar USD 700 a Diego Ruiz. Inténtalo con el saldo actual y cuéntame qué ocurre y qué harías después. | USD 650 | Entiende el rechazo, propone un paso coherente; sin nuevo movimiento | 120 s |
| T6 | Piensas pagar USD 50 a Valentina Paz. Deja la operación lista para comprobar sus datos, pero decides no hacerla. Sal sin que se mueva el dinero. | Panel sin diálogos; USD 650 | Llega a revisión, abandona, no hay cargo | 120 s |

Dependencias: si una tarea previa no termina correctamente, el moderador prepara el estado indicado fuera de la vista del participante y documenta esa intervención antes de iniciar el siguiente tiempo. No contar esa preparación como éxito de la persona ni como ayuda dentro de la siguiente tarea. Si no se puede restaurar, la tarea dependiente queda «no evaluable». T5 incluye un rechazo intencional: ese rechazo no es un error de interacción. Los importes de este plan son escenarios de prueba, no tarifas o valores normativos.

## 7. Operacionalización de métricas

- Resultado por tarea: completada sin ayuda, completada con ayuda, no completada/abandonada, no evaluable por fallo técnico/estado, u omitida por la persona. Pendiente no equivale a fallo.
- Tiempo: desde terminar de leer y comprobar comprensión hasta éxito, abandono o límite; incluye ayuda. Registrar interrupciones externas; excluir esos tiempos de comparación, no necesariamente el resultado. El pensamiento en voz alta afecta los tiempos: usarlos como orientación formativa, no como rendimiento poblacional.
- Error de interacción: elección o entrada que provoca un resultado no deseado y requiere corrección; registrar conducta específica. Exploración deliberada o el rechazo inducido en T5 no son automáticamente errores.
- Ayuda: instrucción que revela cómo completar la tarea. Repetir neutralmente el escenario no cuenta. Un éxito con alguna ayuda no se clasifica sin ayuda.
- Facilidad posterior: «¿Qué tan fácil o difícil te resultó esta tarea?» de 1 (muy difícil) a 7 (muy fácil). Puede no responder. Escala de facilidad del estudio; no calcular SUS a partir de ella ni atribuirle certificación.
- Evidencia: observación y cita breve, separadas de interpretación y propuesta.

Para cada tarea entre participantes: éxito sin ayuda / participantes con resultado evaluable; informar n/N y excluidos. No mezclar pilotos. Ayuda y fallo permanecen en el denominador; omitidas y no evaluables se excluyen y se explican. Calcular mediana de tiempos comparables, separando éxitos sin ayuda de otras condiciones. No convertir respuestas faltantes en cero. El panel resume una sesión; no agrega automáticamente toda la investigación.

## 8. Análisis y decisión

Describir hallazgo → evidencia/códigos → tareas afectadas → gravedad → cambio propuesto → responsable → criterio de nueva prueba.

Gravedad de trabajo: crítico (cargo/destino no deseado o pérdida de control); alto (bloquea una tarea esencial); medio (obliga a ayuda o recuperación); bajo (fricción menor). La frecuencia con cinco personas no estima prevalencia poblacional. Revisar antes de otra ronda cualquier hallazgo crítico y los bloqueos recurrentes. Propuesta interna: buscar al menos 4/5 éxitos sin ayuda en envío, retiro y cancelación; es un objetivo del equipo, no un umbral de un estándar. Informar resultados reales incluso si no alcanzan el objetivo.

Cierre: «¿Qué te generó dudas? ¿Qué creías que ocurría con el dinero? ¿Qué cambiarías primero?». No pedir que confirmen que la interfaz es fácil o confiable.

## 9. Evidencias de entrega

Plan versionado, ficha de reclutamiento sin identificación, registro de aceptación, resultados JSON reales, tabla agregada por tarea, hallazgos priorizados, capturas con datos ficticios y backlog de correcciones. El piloto y la comprobación técnica no cuentan como participantes del estudio. Hasta realizar sesiones, presentar «preparado para evaluación», nunca resultados inventados.

## Referencias

- Nielsen Norman Group: https://www.nngroup.com/articles/usability-test-checklist/ — planificación de objetivos, muestra, tareas, piloto y métricas.
- GOV.UK: https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing — tareas con objetivos y sin revelar el recorrido; observación moderada.
- GOV.UK: https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research — información previa, decisión voluntaria y registro de consentimiento. Referencia metodológica; no declaración de cumplimiento legal en Ecuador.
