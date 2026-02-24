"""MCP transport layer for code-rag root repository."""

from .gateway import BackendClientProtocol, McpGateway

__all__ = ["McpGateway", "BackendClientProtocol"]
