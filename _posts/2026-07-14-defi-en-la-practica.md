---
title: "DeFi en la práctica: cómo funciona pedir prestado, prestar y hacer trades sin un banco de por medio"
date: 2026-07-14 20:00:00 -0700
author: "Alejandro García, MBA"
category: "economía descentralizada"
pillar: "/"
pillar_label: "Ver Infinexa"
keywords: ["qué es DeFi explicado", "finanzas descentralizadas cómo funcionan", "cómo prestar cripto y ganar interés", "intercambio descentralizado explicado", "riesgos de DeFi"]
description: "DeFi no es un activo ni una app — es un conjunto de servicios financieros que corren solos, sin banco ni broker de por medio. Esto es exactamente cómo se ve prestar, pedir prestado y hacer un intercambio en la práctica."
image: "/assets/blog/defi-en-la-practica.webp"
image_alt: "Ilustración de dos billeteras digitales conectadas directamente entre sí sin ningún edificio bancario de por medio, representando un intercambio financiero sin intermediarios"
---

Puedes pedir un préstamo, prestar tu dinero para ganar interés, o cambiar una moneda por otra — sin llenar una solicitud, sin que nadie revise tu historial crediticio, y sin que ningún banco esté en medio de la transacción.
{: .lead}

Eso es, en la práctica, lo que la gente quiere decir cuando habla de DeFi — finanzas descentralizadas. No es un activo que se compra ni una aplicación específica. Es un conjunto de servicios financieros que, en lugar de depender de una institución que apruebe cada operación, corren mediante código que ya está escrito y publicado, disponible para que cualquiera lo use directamente desde su wallet.

El término empezó a usarse alrededor de 2018, cuando los primeros protocolos de este tipo alcanzaron suficiente uso real como para necesitar un nombre propio. Hoy existen decenas de estos protocolos, cada uno enfocado en una función específica — intercambios, préstamos, ahorro con interés — y muchos de ellos se pueden combinar entre sí, porque todos corren sobre la misma infraestructura pública y cualquiera puede construir sobre lo que ya existe.

## Qué significa "finanzas" sin bancos de por medio

Cuando depositas dinero en un banco, el banco decide a quién prestárselo, a qué tasa, y se queda con buena parte de la diferencia entre lo que te paga a ti y lo que le cobra a quien pide prestado. Cuando quieres cambiar una moneda por otra, una casa de cambio o un banco fija el tipo de cambio y cobra una comisión por hacer de intermediario.

En DeFi, esas mismas funciones —prestar, pedir prestado, intercambiar— existen, pero el intermediario ya no es una institución con un edificio y un departamento de crédito. Es un contrato inteligente: un programa publicado en una blockchain que ejecuta exactamente las reglas que tiene escritas, sin que nadie de un lado necesite conocer ni confiar en la persona del otro lado.

## Cómo se ve un intercambio en la práctica

Supón que tienes una moneda digital y quieres cambiarla por otra. En un exchange descentralizado (DEX, por sus siglas en inglés), el proceso se ve así:

<div class="timeline-row">
  <div class="timeline-item"><div class="timeline-dot accent"></div><div class="timeline-label">Conectas tu wallet</div><div class="timeline-text">Sin crear una cuenta ni entregar identificación — la wallet misma es tu identidad en la plataforma.</div></div>
  <div class="timeline-item"><div class="timeline-dot accent"></div><div class="timeline-label">Eliges el par</div><div class="timeline-text">Qué moneda tienes y cuál quieres recibir a cambio.</div></div>
  <div class="timeline-item"><div class="timeline-dot accent"></div><div class="timeline-label">El contrato ejecuta el intercambio</div><div class="timeline-text">Contra una reserva de fondos llamada "pool de liquidez", no contra otra persona esperando del otro lado.</div></div>
  <div class="timeline-item"><div class="timeline-dot accent"></div><div class="timeline-label">Recibes el resultado</div><div class="timeline-text">En segundos, directo en tu wallet — sin esperar aprobación de nadie.</div></div>
</div>

Esa "reserva de fondos" —el pool de liquidez— existe porque otras personas depositaron sus propias monedas ahí, a cambio de recibir una parte de las comisiones que paga cada quien que hace un intercambio. Eso es, en esencia, lo que hace posible que el intercambio ocurra sin que un banco fije el precio.

<div class="principio">
  <div class="principio-badge">1</div>
  <div class="principio-body">
    <div class="principio-label">Lo que te llevas</div>
    <div class="principio-titulo">En DeFi no hay una contraparte humana del otro lado — hay un <em>fondo compartido</em> que cualquiera puede alimentar o usar.</div>
    <p class="principio-texto">Quien pone dinero en ese fondo gana una parte de cada comisión que se cobra. Quien lo usa para intercambiar, paga esa comisión. Ninguno de los dos necesita conocer al otro ni confiar en su palabra — solo confían en que el código haga exactamente lo que dice que hace.</p>
  </div>
  <div class="principio-num">01</div>
</div>

## Prestar y pedir prestado sin pedir permiso

El otro uso más común de DeFi es prestar y pedir prestado. Funciona distinto a un banco en un punto clave: en la mayoría de los protocolos, para pedir prestado necesitas depositar primero una garantía —otra moneda digital— por un valor mayor al que quieres pedir prestado. Si el valor de esa garantía cae demasiado, el protocolo la vende automáticamente para cubrir el préstamo, sin necesidad de que nadie de cobranza te llame.

Del otro lado, quien deposita sus monedas para prestarlas no está haciéndole un favor a nadie en particular — su dinero entra a un fondo común del que cualquiera puede pedir prestado bajo las mismas reglas, y a cambio recibe el interés que paga quien pidió prestado, menos una comisión pequeña del protocolo.

Carlos, después de resolver lo de las remesas de su tía, me preguntó si esto no era básicamente lo mismo que un banco, solo que con otro nombre. La diferencia que le señalé es esta: un banco decide cuánto pagarte por tu dinero y cuánto cobrarle a quien lo pide prestado, y se queda con la diferencia como ganancia propia. Aquí, esa diferencia entre lo que se paga y lo que se cobra la fija el propio mercado de oferta y demanda dentro del protocolo, en tiempo real, visible para cualquiera que quiera revisarlo.

<div class="principio">
  <div class="principio-badge">2</div>
  <div class="principio-body">
    <div class="principio-label">Lo que te llevas</div>
    <div class="principio-titulo">La garantía reemplaza al historial crediticio — <em>nadie revisa quién eres</em>, solo cuánto pusiste de respaldo.</div>
    <p class="principio-texto">Esto tiene una consecuencia práctica importante: no puedes pedir prestado más de lo que ya tienes en garantía. DeFi no resuelve el problema de "necesito dinero que no tengo" — resuelve el problema de "tengo un activo digital y quiero liquidez sin vender ese activo".</p>
  </div>
  <div class="principio-num">02</div>
</div>

## Lo que la conveniencia no elimina

Nada de esto está libre de riesgo, y decirlo con esa claridad importa más que la conveniencia del proceso. Un contrato inteligente es código escrito por personas, y el código puede tener errores — algunos de los ataques más conocidos a protocolos DeFi no fueron fraudes en el sentido tradicional, sino fallas técnicas que alguien más encontró antes que los desarrolladores. Por eso los protocolos más establecidos invierten en auditorías externas de su código, y por eso vale la pena revisar si un protocolo las tiene antes de confiarle dinero.

Tampoco existe un número al que llamar si algo sale mal. No hay un seguro de depósitos, no hay una institución que revierta una transacción equivocada, no hay a quién reclamarle si el valor de tu garantía cae más rápido de lo que puedes reaccionar. La misma ausencia de intermediario que elimina la fricción también elimina la red de protección que ese intermediario normalmente ofrece.

Hay además un riesgo menos evidente para quien aporta liquidez a un pool de intercambio: si el precio de las dos monedas del pool se separa mucho entre sí, quien puso el dinero ahí puede terminar con menos valor total del que hubiera tenido si simplemente se hubiera quedado con sus monedas originales sin depositarlas. Se le llama pérdida impermanente, y es exactamente el tipo de detalle que una explicación superficial de DeFi suele omitir por completo.

Esto no es distinto, en el fondo, de lo que ya vimos con las wallets no custodiales: el control total viene acompañado de responsabilidad total. La diferencia es que ahí hablábamos de guardar tu dinero — aquí hablamos de moverlo activamente, prestarlo, pedirlo prestado, y eso multiplica los lugares donde algo puede salir distinto a lo esperado.

Entender esto no es una razón para evitarlo ni para lanzarse sin pensar — es la base mínima de información con la que cualquier persona debería decidir si esto tiene sentido para su situación. Si quieres ver cómo encaja esto en el resto de la nueva economía digital, de eso se trata [Infinexa](/) — y si ya tienes una pregunta concreta sobre tu propio caso, esa es una conversación que vale la pena tener directamente.
