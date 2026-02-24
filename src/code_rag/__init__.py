"""Thin MCP layer package for code-rag root repository."""

from .mcp.gateway import BackendClientProtocol, McpGateway

__all__ = ["McpGateway", "BackendClientProtocol"]
