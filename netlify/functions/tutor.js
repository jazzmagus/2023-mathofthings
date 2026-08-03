const richiestePerIP = new Map();
const LIMITE = 40;
const FINESTRA_MS = 60 * 60 * 1000;

function troppeRichieste(ip) {
  const ora = Date.now();
  const voce = richiestePerIP.get(ip);
  if (!voce || ora - voce.inizio > FINESTRA_MS) {
    richiestePerIP.set(ip, { inizio: ora, conteggio: 1 });
    return false;
  }
  voce.conteggio += 1;
  return voce.conteggio > LIMITE;
}

export default async (request, context) => {
  if (request.method !== "POST") {
    return new Response("Metodo non consentito", { status: 405 });
  }

  const ip = context.ip || request.headers.get("x-nf-client-connection-ip") || "sconosciuto";
  if (troppeRichieste(ip)) {
    return new Response(JSON.stringify({ error: "Troppe richieste, riprova più tardi." }), {
      status: 429,
      headers: { "content-type": "application/json" }
    });
  }

  const corpo = await request.json();

  const risposta = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "x-api-key": Netlify.env.get("ANTHROPIC_API_KEY"),
      "anthropic-version": "2023-06-01"
    },
    body: JSON.stringify({
      model: corpo.model,
      max_tokens: corpo.max_tokens,
      system: corpo.system,
      messages: corpo.messages
    })
  });

  return new Response(await risposta.text(), {
    status: risposta.status,
    headers: { "content-type": "application/json" }
  });
};

export const config = { path: "/api/tutor" };
