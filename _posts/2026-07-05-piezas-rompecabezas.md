---
title: "Las piezas sueltas de un rompecabezas de 30 años"
author: "Alejandro García, MBA"
category: "historia y tecnología"
pillar: "/infografia"
pillar_label: "Ver El Patrón"
keywords: ["historia de bitcoin antes de bitcoin", "precursores de bitcoin", "diffie hellman criptografía historia", "hashcash adam back", "b-money wei dai historia criptomonedas"]
description: "Bitcoin no apareció de la nada en 2009. Fue el último paso de un rompecabezas que cinco personas distintas, en tres décadas, habían estado armando sin saberlo."
image: "/assets/blog/piezas-rompecabezas.webp"
image_alt: "Ilustración de cinco piezas de rompecabezas flotando separadas, cada una con una fecha entre 1976 y 1998, que convergen hacia un punto central"
---

Mucho antes de que existiera Bitcoin, ya existían todas las piezas para construirlo. Lo que faltaba no era tecnología — era alguien que las conectara todas en el orden correcto.
{: .lead}

Eso tardó treinta años en suceder. Y cada pieza la puso una persona distinta, en un momento distinto, sin saber exactamente para qué terminaría siendo útil. Esta es la historia de esas piezas — y de por qué entenderlas cambia completamente cómo se ve lo que está pasando hoy.

## El problema que nadie había resuelto: ¿cómo confiar en alguien que no conoces?

Durante miles de años, la confianza entre personas que no se conocían requirió un intermediario: un banco, un notario, un gobierno, una institución que dijera "este mensaje viene de quien dice venir, y esta promesa vale". Sin ese intermediario, no había forma de verificar nada.

Eso cambió en 1976, cuando Whitfield Diffie y Martin Hellman publicaron un paper titulado *"New Directions in Cryptography"* que resolvía algo que hasta entonces parecía imposible: dos personas podían establecer un código secreto compartido sin haberse visto nunca, sin haber hablado antes, y sin que nadie que interceptara su comunicación pudiera descifrarla.

La idea detrás es elegante: cada persona tiene dos llaves matemáticamente relacionadas — una pública, que puede compartir con el mundo, y una privada, que guarda solo ella. Lo que una llave cifra, solo la otra puede descifrar. Así, cualquiera puede enviarte un mensaje que solo tú puedes leer, sin que necesites haberle dado tu llave secreta.

Por primera vez en la historia, la confianza digital podía existir sin un intermediario humano. Esa fue la primera pieza.

<div class="principio">
  <div class="principio-badge">1</div>
  <div class="principio-body">
    <div class="principio-label">Lo que te llevas</div>
    <div class="principio-titulo">La confianza digital nació en 1976 — <em>no en 2009</em>.</div>
    <p class="principio-texto">Antes de Diffie y Hellman, verificar que un mensaje venía de quien decía venir requería un intermediario. Después de ellos, las matemáticas podían hacer ese trabajo solas. Ese cambio es la semilla de todo lo que hoy llamamos "sin banco de por medio".</p>
  </div>
  <div class="principio-num">01</div>
</div>

## 1982: el problema de los generales que no se conocen

Resolver la confianza entre dos personas fue un avance enorme. Pero ¿qué pasa cuando son diez? ¿O mil? ¿Cómo se pone de acuerdo un grupo grande de participantes que no se conocen entre sí, cuando cualquiera de ellos podría estar mintiendo?

En 1982, Leslie Lamport, junto con Robert Shostak y Marshall Pease, formalizó este problema en un paper que lo llamó "El Problema de los Generales Bizantinos". La metáfora: un grupo de generales que rodean una ciudad enemiga necesitan coordinarse para atacar al mismo tiempo — pero sus mensajeros pueden ser interceptados o corrompidos, y algunos generales podrían ser traidores. ¿Cómo se aseguran de que todos actúen en conjunto, sin un comandante central que les diga qué hacer?

El paper no solo planteó el problema — propuso las condiciones matemáticas bajo las cuales es posible resolverlo. Y aunque en 1982 nadie pensaba en monedas digitales, estaban describiendo exactamente el desafío técnico central que Bitcoin resolvería 27 años después: cómo lograr consenso entre miles de participantes desconocidos, sin que ninguno tenga que confiar en los demás.

## 1997: una solución para el spam que terminó siendo algo mucho más grande

A mediados de los 90, el correo electrónico se había llenado de spam — mensajes masivos enviados con costo cero para quien los mandaba. Adam Back, criptógrafo británico, propuso en 1997 una solución llamada Hashcash: para enviar un correo, el remitente tendría que resolver un pequeño problema matemático que consumiera unos segundos de procesamiento de su computadora.

Para un usuario normal enviando un correo, unos segundos no son nada. Para alguien enviando diez millones de correos de spam, ese costo computacional acumulado hace el negocio inviable. La solución funciona porque hace que el trabajo tenga un costo real — aunque ese costo sea solo tiempo de procesamiento, no dinero.

Lo que Back no sabía en 1997 es que estaba inventando lo que después se llamaría "prueba de trabajo" — el mecanismo exacto que Bitcoin usaría para validar transacciones y hacer que falsificar el registro histórico fuera computacionalmente imposible. Satoshi Nakamoto lo citó directamente en el whitepaper de Bitcoin once años después.

<div class="principio">
  <div class="principio-badge">2</div>
  <div class="principio-body">
    <div class="principio-label">Lo que te llevas</div>
    <div class="principio-titulo">Las mejores innovaciones casi nunca resuelven el problema para el que fueron diseñadas — <em>resuelven uno que todavía no existe</em>.</div>
    <p class="principio-texto">Hashcash fue diseñado para el spam. Terminó siendo el motor de Bitcoin. Este patrón — una solución que encuentra su problema real años después — aparece una y otra vez en la historia de la tecnología. Ya lo conoces: es El Patrón.</p>
  </div>
  <div class="principio-num">02</div>
</div>

## 1998: dos personas describen Bitcoin, una década antes de que existiera

En 1998, casi al mismo tiempo, dos personas publicaron propuestas de sistemas de dinero digital descentralizado que describían, en papel, casi todo lo que sería Bitcoin.

Wei Dai publicó b-money — un documento de una sola página que proponía un sistema donde cualquier participante pudiera crear dinero resolviendo problemas computacionales, y donde las transacciones fueran verificadas colectivamente por todos los participantes en lugar de por una autoridad central. Nadie lo implementó. Nadie le hizo caso en su momento.

Nick Szabo, por su parte, trabajó durante varios años en un concepto que llamó Bit Gold — una propuesta más detallada que combinaba prueba de trabajo, registros distribuidos, y firmas digitales para crear valor digital escaso sin respaldo en metal ni en promesas de ningún gobierno. Szabo también introdujo en esta época el concepto de "contrato inteligente" — un acuerdo que se ejecuta automáticamente cuando se cumplen ciertas condiciones, sin que nadie tenga que hacer cumplir nada. Bit Gold tampoco llegó a implementarse.

Carlos leyó sobre esto y preguntó lo obvio: si ya tenían la idea completa en 1998, ¿por qué tardaron diez años en construirlo? La respuesta tiene dos partes. Una técnica: faltaba resolver de forma elegante el doble gasto sin un servidor central de confianza. Y una de contexto: el mundo no estaba prestando atención — hasta que un colapso financiero de escala global lo obligó a hacerlo.

<div class="principio">
  <div class="principio-badge">3</div>
  <div class="principio-body">
    <div class="principio-label">Lo que te llevas</div>
    <div class="principio-titulo">Tener razón demasiado pronto es, en la práctica, <em>lo mismo que estar equivocado</em>.</div>
    <p class="principio-texto">b-money y Bit Gold describieron Bitcoin antes de que existiera. Nadie los adoptó porque el contexto no estaba listo. El timing no es un detalle — es, con frecuencia, la variable que decide si una idea correcta se convierte en algo real o desaparece sin dejar rastro.</p>
  </div>
  <div class="principio-num">03</div>
</div>

## Treinta años de trabajo invisible

En 2008, cuando alguien bajo el seudónimo Satoshi Nakamoto publicó el whitepaper de Bitcoin, no estaba inventando de cero. Estaba conectando piezas que ya existían: las firmas digitales de Diffie y Hellman, el problema de consenso de Lamport, la prueba de trabajo de Adam Back, las ideas de dinero digital de Dai y Szabo.

Lo que Satoshi resolvió — de forma elegante, en nueve páginas — fue el único problema que los demás no habían logrado cerrar del todo: cómo evitar que alguien gastara la misma moneda digital dos veces, sin necesitar un servidor central que llevara el registro. Esa solución se llama blockchain, y la veremos en el siguiente post de esta serie.

Hay algo que vale la pena nombrar antes de cerrar: ninguno de los cinco — Diffie, Hellman, Lamport, Back, Dai, Szabo — sabía que estaba construyendo el rompecabezas. Cada uno resolvía un problema que tenía frente a sí. La conexión entre sus trabajos solo se volvió visible en retrospectiva, cuando alguien los unió todos.

Dos formas de seguir desde aquí: si quieres ver este mismo patrón —piezas que parecen desconectadas hasta que alguien las une— en otras eras de la historia tecnológica, eso es exactamente lo que muestra [El Patrón](/infografia). Y el siguiente post de esta serie entra directo al momento en que una de esas ideas —el dinero digital— sí llegó a implementarse, funcionó durante casi una década, y aun así desapareció.
