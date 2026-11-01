from ..config import settings
from .clients import clients
from .prompts import SYSTEM_PROMPT
from .retriever import executeQuery


def formatContext(contexto: list[object]) -> str:
    lineas = []
    for m in contexto:
        meta = getattr(m, "metadata", None) or {}
        if isinstance(meta, dict):
            titulo = meta.get("titulo", "")
            contenido = meta.get("contenido", "")
        else:
            titulo = getattr(meta, "titulo", "")
            contenido = getattr(meta, "contenido", "")
        lineas.append(f"- {titulo}: {contenido}")
    return "\n".join(lineas)


def callLLM(query: str, contexto: list[object]):
    contexto_txt = formatContext(contexto)
    completion = clients.groqAIclient.chat.completions.create(
        model=settings.groqModel,
        messages=[
            {"role": "system", "content": f"reglas: {SYSTEM_PROMPT}"},
            {
                "role": "user",
                "content": f"contexto:\n{contexto_txt}\n\npregunta:\n{query}",
            },
        ],
    )

    return completion.choices[0].message.content


def pipelineResponse(query: str):
    try:
        contexto = executeQuery(query)
        response = callLLM(query, contexto)
        return response
    except Exception as e:
        raise RuntimeError(
            "algo salio mal con algun proceso relacionado al flow del rag"
        ) from e


if __name__ == "__main__":
    response = pipelineResponse("quien gano la champions de 2016?")
    print(response)
