# Action Labs — Web

Web comercial de **Action Labs**: consultoría e implementación de IA para empresas (agentes, automatizaciones y sistemas de datos), desplegado en la infraestructura del cliente.

## Páginas

| Fichero | Contenido |
|---|---|
| `index.html` | Landing: hero, propiedad del stack, valor, agentes, 8 aplicaciones de IA, tecnologías, integraciones, proceso, casos reales, quién está detrás, FAQ, contacto |
| `formacion.html` | Hub de formación |
| `curso-chatgpt-empresas.html`, `curso-ia.html`, `formacion-ia-empresas.html`, `formacion-claude.html` | Páginas de curso con formulario de información |
| `newsletter.html` | Suscripción (viernes 12:00) |
| `legal.html` · `404.html` · `robots.txt` · `sitemap.xml` | Legal, error y SEO |
| `content.json` | Textos ES/EN (el diccionario embebido en cada HTML debe mantenerse sincronizado) |
| `build-assets/` | Logo/ilustraciones (`assets.json`), robots, 46 logos de software, 16 de IA, colores de marca |

## Funcionamiento

- **Bilingüe ES/EN**, español por defecto, preferencia en `localStorage`, `?lang=en` para forzar.
- **Calendario de reserva** propio (estilo Calendly) en modal: día laborable → hora (mañana/tarde) → formulario. Sin backend.
- **Todos los envíos van a `ralcaraz.canals@gmail.com`** vía FormSubmit (reserva, contacto, captación de email, info de cursos, newsletter), cada uno con su asunto.
  - ⚠️ **Activación pendiente**: el primer envío real dispara el correo de confirmación de FormSubmit; hay que hacer clic una vez.
  - La confirmación al usuario **no es automática**: hay que responder al email (la web promete respuesta en 24 h).
- **Contacto**: formulario, reserva de llamada, WhatsApp, teléfono y email, todos visibles.
- **Regla del sitio**: ningún dato, cliente o métrica inventado.

## Local

```bash
python3 -m http.server 5098
# → http://localhost:5098
```
