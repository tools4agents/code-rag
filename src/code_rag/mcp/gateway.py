"""Thin MCP gateway over external code-rag backend service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class BackendClientProtocol(Protocol):
    """Protocol for backend service client used by MCP layer."""

    def call(self, *, method: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Execute backend method and return response payload.

        Args:
            method: Backend operation identifier.
            payload: Request payload.

        Returns:
            dict[str, Any]: Response payload.
        """


@dataclass(slots=True)
class McpGateway:
    """Thin transport adapter from MCP calls to backend service client."""

    backend: BackendClientProtocol

    def invoke(self, *, method: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Forward MCP request to backend service without domain logic.

        Args:
            method: Backend operation identifier.
            payload: Request payload.

        Returns:
            dict[str, Any]: Backend response.
        """
        return self.backend.call(method=method, payload=payload)
