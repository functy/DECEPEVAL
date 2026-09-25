from __future__ import annotations

def _signature_to_html(
    name: str,
    object_type: str,
    signature: inspect.Signature | None,
    decorators: list[str],
) -> str:
    parts = []
    parts.append("<span class='function-signature'>")
    for decorator in decorators:
        parts.append(
            f"<span class='function-decorator'>@{decorator}</span><br>"
        )
    parts.append(
        f"<span class='is-italic'>{object_type}</span> "
        f"<span class='has-text-weight-bold'>{name}</span>("
    )
    if not signature:
        parts.append("<span class='param-name'>self</span>)")
        parts.append("</span>")
        return None
    for i, param in enumerate(signature.parameters.values()):
        parts.append(f"<span class='param-name'>{escape(param.name)}</span>")
        annotation = ""
        if param.annotation != inspect.Parameter.empty:
            annotation = escape(str(param.annotation))
            parts.append(
                f": <span class='param-annotation'>{annotation}</span>"
            )
        if param.default != inspect.Parameter.empty:
            default = escape(str(param.default))
            if annotation == "str":
                default = f'"{default}"'
            parts.append(f" = <span class='param-default'>{default}</span>")
        if i < len(signature.parameters) - 1:
            parts.append(", ")
    parts.append(")")
    if signature.return_annotation != inspect.Signature.empty:
        return_annotation = escape(str(signature.return_annotation))
        parts.append(
            f": -> <span class='return-annotation'>{return_annotation}</span>"
        )
    parts.append("</span>")
    return "".join(parts)
