# Caleta · Tu dinero, en casa

Dirección creativa inicial, 16 de noviembre de 2026. Aplicada a la portada y la cuenta de práctica. Pendiente validación con usuarios ecuatorianos.

## Concepto

Casa, cercanía y autonomía. La marca acompaña a quien trabaja con el mundo y mantiene sus vínculos en Ecuador. El hogar es el símbolo principal; montaña, agua, sol y terracota forman una ilustración original y abstracta, sin representar una localidad específica ni atribuir motivos a una comunidad.

Mensaje principal: «Tu mundo crece. Tu dinero, en casa». Firma: «De aquí. Para llegar más lejos». Voz: directa, cálida, serena. El giro «¡Listo, de una!» aparece solo como celebración breve; importes, destinatarios, errores y condiciones usan lenguaje preciso.

## Sistema visual

| Token | Valor | Uso |
|---|---|---|
| Pacífico | #214e47 | Botones principales y saldo |
| Tinta | #203f3b | Texto principal |
| Arena | #f8f5ed | Fondo |
| Terracota | #ac593c | Marca y acentos |
| Sol | #eed19a | Acentos suaves |
| Línea | #e4e6da | Separadores |

Símbolo: casa de trazo abierto y simple. Wordmark: minúsculas, compacto, punto terracota. Ilustración SVG propia, reutilizable en `public/caleta-landscape.svg`. Tarjetas de 20 px de radio; controles de 10 px. Jerarquía: saldo y acción, luego movimientos. Tipografía de sistema en la demo autónoma; la portada conserva la tipografía del proyecto.

## Movimiento

Carácter sereno y funcional. Curva: cubic-bezier(.2,0,0,1). Duraciones: 150 ms para respuesta de controles, 320 ms para diálogos, 550 ms para resolución de transacción simulada. Entrada suave hacia arriba, sin rebotes. Secuencia: preparar → revisar → simular → comprobante → saldo e historial resaltados.

El saldo se registra una sola vez al confirmar; el breve estado «Simulando» es presentación local, no actividad bancaria. Se bloquean confirmaciones repetidas durante esa transición. `prefers-reduced-motion` elimina animaciones y la espera visual. Los diálogos conservan foco de teclado y lo devuelven a la acción al cerrar el comprobante.

## Alcance y próximos tests

Se mantiene explícita la naturaleza ficticia en banner, acciones y comprobantes. Ninguna promesa de pagos reales. Evaluar comprensión de «mi Caleta», confianza, legibilidad móvil, descubrimiento de envío/retiro, comprensión de confirmación y percepción del tono local. La dirección visual aún no constituye validación de marca ni resultados de usabilidad.
