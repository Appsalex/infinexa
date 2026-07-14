# PROMPT PARA CLAUDE CODE
## INFINEXA — FASE 1.5: CONSOLIDACIÓN, MEDICIÓN Y CAPTACIÓN

> Guardado el 13 de julio de 2026. Gobierna la Fase 1.5 (consolidación posterior al
> reposicionamiento de la Fase 1, cuyo prompt vive en
> `PROMPT_MAESTRO_REPOSICIONAMIENTO_13JUL2026.md`). La comparación punto por punto contra
> lo ejecutado vive en `BITACORA.md` y `ESTADO.md`.

Actúa como un equipo senior coordinado de producto, UX, desarrollo frontend, arquitectura web, analítica, SEO técnico, accesibilidad, conversión y QA.
Trabaja también como el desarrollador principal responsable de implementar directamente los cambios en el repositorio actual de Infinexa.
No debes volver a analizar ni redefinir el posicionamiento general de la marca.
La transformación estratégica ya fue realizada y está publicada.
Tu objetivo ahora es:
> **Consolidar la nueva identidad de Infinexa mediante páginas propias, captación estructurada, analítica completa, SEO técnico, accesibilidad, experiencia móvil y mejor arquitectura editorial.**
No entregues únicamente recomendaciones.
Debes:
1. Auditar el estado actual.
2. Confirmar el commit y la rama de trabajo.
3. Congelar el alcance.
4. Implementar directamente.
5. Validar.
6. Documentar.
7. Entregar un reporte final preciso.

---

# 1. CONTEXTO ACTUAL

Infinexa ya fue reposicionada. Actualmente es:
> Una plataforma independiente de educación, criterio y conexión sobre dinero, blockchain, Web3, inteligencia artificial y nuevos modelos de creación de valor.

Hand4Hand fue eliminado completamente del sitio público.

Ya se encuentran publicados: nueva página principal, propuesta de valor renovada, tres rutas (Comprender, Evaluar, Aplicar), diagnóstico básico, talleres, perfil de Alejandro, Diversifica reposicionado, Infografía corregida, Infinexa Digital, blog con 15 publicaciones, páginas legales, GA4, ocho eventos de conversión, diseño responsive, navegación y footer unificados visualmente.

El sitio está publicado en `https://infinexa.app/`. El repositorio contiene cambios desde el commit `06747d6`. No asumir que ese es necesariamente el commit actual — verificar primero `git log`, `git status` y la rama activa.

---

# 2. PRINCIPIO RECTOR

> **No reabrir la estrategia. Consolidar lo que ya está funcionando.**

Prioridad: captar datos propios, mejorar medición, crear páginas compartibles, fortalecer SEO, mejorar accesibilidad, mejorar experiencia móvil, organizar el contenido, dejar una base reutilizable.

No agregar: academia, membresía, dashboard, IA personalizada, CRM completo, marketplace, wallet conectada, nuevos proyectos, Hand4Hand, autódromo, landing pages de oportunidades, aplicación móvil, multiidioma, pagos de cursos, funciones no incluidas expresamente en este prompt. Toda idea adicional debe registrarse en el backlog.

---

# 3. OBJETIVO DE LA FASE 1.5

Al finalizar: (1) páginas dedicadas para las rutas principales, (2) captación de correo y consentimiento antes de WhatsApp, (3) formularios funcionales, (4) eventos de conversión completos y documentados, (5) canonicals, (6) JSON-LD, (7) mejor navegación editorial, (8) componente reutilizable de siguiente artículo, (9) mejoras de accesibilidad, (10) pruebas reales en móvil y escritorio, (11) reducción de HTML duplicado cuando sea viable, (12) build limpio, (13) sitio listo para continuar recibiendo tráfico y medir comportamiento real.

---

# 4. REGLAS DE EJECUCIÓN

No repetir el análisis estratégico, no reescribir la propuesta de valor, no cambiar la identidad, no rediseñar toda la página, no reabrir decisiones cerradas, no cambiar el stack, no actualizar dependencias sin necesidad, no eliminar contenido de valor, no agregar funciones futuras, no producir un informe largo antes de comenzar.

Cuando falte información no crítica: declarar el supuesto, usar una solución reversible, continuar, registrar el pendiente.

Solo detener por: riesgo de pérdida de datos, error de seguridad grave, falta de acceso indispensable, repositorio en estado inconsistente, dependencia externa obligatoria, conflicto no resuelto con cambios existentes.

---

# 5. AUDITORÍA INICIAL OBLIGATORIA

Antes de modificar: `git status`, `git log --oneline -10`, rama activa, stack, framework, estructura de rutas, layouts, componentes reutilizables, formularios actuales, integración GA4, eventos existentes, sitemap, robots, páginas legales, estructura del blog, metadatos, CSS responsive, accesibilidad, estado del build, enlaces internos, duplicación de navegación y footer. No mostrar secretos. Entregar diagnóstico breve (estado del repo, stack, bloqueantes, archivos principales, alcance congelado, orden de implementación) y continuar directamente con la implementación.

---

# 6. PÁGINAS DEDICADAS

Crear páginas propias para `/diagnostico/`, `/talleres/`, `/nosotros/`, `/contacto/`, `/aprender/`. Conservar anclas actuales cuando sean útiles, dirigiendo correctamente a las nuevas páginas.

**6.1 `/diagnostico/`** — explicación del Mapa de Preparación, beneficio, dimensiones evaluadas (educación financiera, comprensión de blockchain, seguridad digital, wallets, riesgo, objetivos, experiencia práctica, interés principal), tiempo estimado, aviso educativo, formulario/cuestionario, resultado básico, captura de contacto, consentimiento, CTA posterior, WhatsApp contextual opcional. Recomendación entre Comprender/Evaluar/Aplicar, sin recomendar empresas o proyectos específicos.

**6.2 `/talleres/`** — tipos de talleres, para quién, modalidad, temas (educación financiera, blockchain para principiantes, wallets y seguridad, Web3 para empresarios, IA y negocios, diversificación, finanzas tradicionales y descentralizadas, nuevos modelos de creación de valor), beneficios, registro de interés, formulario, consentimiento, confirmación, próximos pasos. No inventar fechas de eventos.

**6.3 `/nosotros/`** — qué es Infinexa, propósito, principios, perfil de MBA Alejandro García, trayectoria, enfoque, qué hace/no hace Infinexa, CTA hacia diagnóstico o contacto. No inventar credenciales.

**6.4 `/contacto/`** — formulario, WhatsApp, correo, tema de interés, motivo, ciudad, país, consentimiento, confirmación, mensaje de privacidad.

**6.5 `/aprender/`** — hub editorial que organiza contenidos por rutas (dinero e inflación, diversificación, historia económica, blockchain, Bitcoin, wallets, stablecoins, seguridad, DeFi, Web3, IA, desarrollo empresarial, aplicación práctica), enlazando al blog y artículos relevantes.

---

# 7. CAPTACIÓN ESTRUCTURADA

Implementar captación previa cuando corresponda, con campos mínimos (nombre, correo, país, ciudad, tema de interés, nivel de experiencia, objetivo, principal duda, consentimiento, fuente de conversión, UTM source/medium/campaign, fecha) — sin pedir todos los campos si genera fricción excesiva. Formularios distintos según intención:

- **Diagnóstico:** nombre, correo, país, nivel, objetivo, consentimiento.
- **Talleres:** nombre, correo, ciudad, taller de interés, modalidad, consentimiento.
- **Contacto:** nombre, correo, tema, mensaje, país, consentimiento.
- **Infinexa Digital:** nombre, correo, empresa, tipo de proyecto, presupuesto aproximado, objetivo, consentimiento.

**Regla de WhatsApp:** WhatsApp debe ser opción posterior o complementaria. Después de enviar el formulario: registrar/enviar los datos, mostrar confirmación, ofrecer abrir WhatsApp con mensaje contextual prellenado. El sistema no debe perder el contacto si el usuario no termina enviando el mensaje en WhatsApp.

---

# 8. DESTINO DE LOS FORMULARIOS

Auditar la arquitectura existente y seleccionar la solución más simple: endpoint serverless, form provider ya existente, correo transaccional, Google Sheets mediante integración segura, backend ligero, almacenamiento estructurado. No agregar una base de datos compleja si no es necesaria. Debe existir: validación server-side cuando sea posible, protección antispam, sanitización, confirmación de envío, manejo de error, estado de carga, consentimiento, evitar exponer credenciales. Documentar dónde llegan los contactos, qué datos se guardan/no se guardan, cómo se elimina o corrige un registro, qué integración se utiliza.

---

# 9. ANALÍTICA

GA4 ya conectado (`G-X8LW9B8JP2`) — no reemplazar la propiedad. Conservar eventos existentes: `hero_primary_cta_clicked`, `hero_secondary_cta_clicked`, `whatsapp_clicked`, `conversation_requested`, `digital_services_opened`, `diagnostic_started`, `diagnostic_completed`, `workshop_interest_submitted`.

Agregar (prioridad alta): `learn_path_selected`, `evaluate_path_selected`, `apply_path_selected`, `contact_form_submitted`, `article_opened`, `next_article_clicked`, `digital_services_lead_submitted`, `risk_page_opened`, `transparency_page_opened`, `founder_profile_opened`. Agregar también cuando exista la interacción: `conference_interest_submitted`, `diversification_assessment_started`, `innovation_guide_opened`.

`article_completed` — no implementar de forma arbitraria; definir una regla confiable (ej. 80% de scroll, mínimo de tiempo razonable, visualización del final del artículo) y documentar la metodología.

No enviar en los eventos: nombre, correo, mensajes, wallets, datos personales o sensibles. Solo contexto no identificable (página, ruta, categoría, tipo de CTA, fuente, estado del formulario).

---

# 10. SEO TÉCNICO

**Canonicals** — cada página indexable con canonical absoluto propio.

**JSON-LD** — Home: `WebSite`/`Organization`/`Person` (sin propiedades no verificables). Blog: `Article`/`BlogPosting` con autor, fecha de publicación/modificación, imagen, descripción, URL, publisher. Navegación: `BreadcrumbList`. Talleres: no usar `Event` hasta que exista fecha/ubicación/evento real.

**Otros** — titles y descriptions únicos, Open Graph, Twitter Cards, alt text, sitemap, robots, redirecciones, H1 único, headings semánticos, URLs consistentes, sin páginas huérfanas, metadatos de artículos, fecha de actualización. No generar contenido duplicado.

---

# 11. BLOG Y ARQUITECTURA EDITORIAL

No reescribir los 15 artículos. Implementar sistema reutilizable para categoría, autor, fecha, fecha de actualización, tiempo de lectura, breadcrumbs, artículo anterior/siguiente, ruta de aprendizaje, CTA educativo, fuentes, aviso educativo.

**Artículo siguiente** — debe funcionar en los 15 artículos, construido mediante layout/include/partial/datos estructurados/front matter — no copiando HTML manualmente en cada uno.

**Ruta editorial** — organizar los artículos en una secuencia lógica (ej. historia del dinero → inflación → diversificación → Bitcoin → blockchain → nodos y minería → wallets → stablecoins → seguridad → DeFi → Web3 → aplicación práctica), sin forzar una secuencia cuando el artículo no corresponda.

**Eventos** — `article_opened`, `next_article_clicked`, `article_completed` según la metodología definida.

---

# 12. COMPONENTES REUTILIZABLES

Auditar si navegación, footer, CTA, formularios y metadatos están duplicados. Cuando sea viable dentro del stack actual, crear componentes/includes reutilizables para header, navegación móvil, footer, CTA, formularios, breadcrumbs, autor, artículo siguiente, aviso educativo, metadatos, analítica. No migrar de framework. No hacer una refactorización masiva si compromete estabilidad — el objetivo es reducir mantenimiento, no rehacer el proyecto.

---

# 13. ACCESIBILIDAD

Implementar: `prefers-reduced-motion`, focus visible, navegación por teclado, labels, `aria-describedby` en errores, `aria-live` para confirmaciones, contraste, tamaños táctiles, skip link, H1 único, jerarquía semántica, alt text, estados de carga/error, botones con nombres accesibles, links diferenciables, no depender solo del color, menú móvil accesible, cierre con Escape cuando corresponda. No agregar ARIA redundante.

---

# 14. EXPERIENCIA MÓVIL

Probar como mínimo estas anchuras: 320px, 375px, 390px, 768px, 1024px, 1440px. Verificar hero, menú, formularios, tarjetas, CTA, botones, modales, blog, tablas, footer, QR, textos, desbordamientos, tamaños táctiles, teclado móvil, mensajes de error. Cuando el entorno lo permita, revisar Chrome móvil / Safari móvil o emulación equivalente. Documentar qué fue probado realmente. No afirmar pruebas en dispositivo físico si no se hicieron.

---

# 15. PÁGINAS LEGALES Y TRANSPARENCIA

Verificar y mejorar `/transparencia/`, `/riesgos/`, `/privacidad/`, `/terminos/`. Añadir enlaces desde footer, formularios, diagnóstico, talleres, contacto, Infinexa Digital. Implementar eventos `risk_page_opened`, `transparency_page_opened`. No convertir textos generales en asesoría legal definitiva — incluir "revisión legal profesional recomendada" cuando corresponda.

---

# 16. SITUACIÓN DE CARLOS

No reconstruir su landing. No restaurar el subdominio. No agregar Hand4Hand. Registrar en documentación interna: que existió una landing personalizada, que fue retirada por reposicionamiento de marca, que cualquier nueva landing específica debe operar fuera de la identidad central de Infinexa, que debe existir comunicación previa con el interesado. No exponer información personal innecesaria.

---

# 17. VALIDACIÓN TÉCNICA

Ejecutar los comandos disponibles correspondientes al proyecto: instalación (solo si hace falta), lint, typecheck, tests, build, revisión de rutas/enlaces/formularios/eventos/consola/sitemap/canonicals/JSON-LD/accesibilidad/responsive, búsqueda final de Hand4Hand, `git diff`, `git status`. Si el proyecto no tiene alguno de estos scripts, decirlo claramente. No inventar resultados. No ocultar warnings. No actualizar dependencias sin necesidad.

---

# 18. CRITERIOS DE CIERRE

Fase 1.5 terminada cuando: las 5 páginas nuevas funcionan; los formularios captan correo y consentimiento; WhatsApp es complementario; los contactos llegan a un destino verificable; los eventos prioritarios están configurados sin datos personales; cada página tiene canonical; JSON-LD implementado; los artículos tienen navegación siguiente; el blog tiene rutas editoriales; `prefers-reduced-motion` implementado; navegación por teclado funciona; formularios tienen estados; experiencia móvil probada; sitemap actualizado; páginas legales enlazadas; sin referencias a Hand4Hand; validaciones disponibles ejecutadas; repositorio documentado; sitio listo para publicar.

---

# 19. OBJETIVOS DE CALIDAD

| Dimensión | Estado anterior | Objetivo Fase 1.5 |
|---|---:|---:|
| Identidad verbal | 8.5 | 9 |
| Claridad inicial | 8.5 | 9 |
| Propuesta de valor | 9 | 9 |
| Independencia de marca | 9.5 | 10 |
| Confianza | 8.5 | 9 |
| Transparencia | 8.5 | 9 |
| UX | 8 | 9 |
| UI | 8 | 8.5 |
| Conversión | 7.5 | 8.5 |
| Arquitectura de contenido | 8 | 9 |
| Blog | 8 | 9 |
| Accesibilidad | 7 | 8.5 |
| SEO técnico | 6 | 8.5 |
| Escalabilidad de marca | 8.5 | 9 |
| Cumplimiento de claims | 9 | 9 |
| Experiencia móvil | 7.5 | 9 |

No ajustar artificialmente las calificaciones. Para cada dimensión explicar: qué cambió, evidencia, resultado, pendiente real, qué faltaría para llegar a 10.

---

# 20. BACKLOG — NO CONSTRUIR EN ESTA FASE

Glosario, calculadoras, newsletter, lead magnets, diagnóstico avanzado, calendario de eventos, registro y pago de talleres, rutas educativas personalizadas, academia, membresía, comunidad, dashboard, certificados, IA educativa, CRM, landings de proyectos, autódromo, Hand4Hand, multiidioma, aplicación móvil. No mezclar estos elementos con la Fase 1.5.

---

# 21. REPORTE FINAL OBLIGATORIO

Resumen (objetivo, resultado, estado de publicación); Repositorio (rama, commit inicial/final, estado de Git); Páginas (creada/funcional/formulario/analítica/SEO/accesibilidad por cada una de las 5); Captación (campos, destino, consentimiento, antispam, confirmación, error, WhatsApp); Analítica (eventos conservados/agregados/pendientes, metodología de article_completed); SEO (canonicals, JSON-LD, sitemap, robots, Open Graph, breadcrumbs, metadatos); Blog (artículos conservados, artículo siguiente, categorías, rutas, eventos); Accesibilidad (reduced motion, teclado, focus, formularios, contraste, ARIA, resultados); Móvil (anchuras probadas, navegadores/emuladores, hallazgos, correcciones); Archivos (creados/modificados/eliminados, redirecciones); Validaciones (lint, typecheck, tests, build, rutas, enlaces, formularios, eventos, SEO, accesibilidad, Hand4Hand); Riesgos (pendientes, limitaciones, dependencias, revisión legal); Calificaciones (tabla anterior vs. nueva); Dictamen (11 preguntas + GO/GO WITH CONDITIONS/NO-GO).

---

# 22. INSTRUCCIÓN FINAL

Comenzar con: auditoría breve, confirmación de Git, identificación de bloqueantes, alcance congelado, implementación directa, validación, reporte final. No esperar nuevas confirmaciones entre bloques salvo bloqueante real. No volver a discutir el posicionamiento de Infinexa. No agregar nuevas líneas de producto. Consolidar, medir, captar y dejar el sitio listo para su siguiente etapa.
