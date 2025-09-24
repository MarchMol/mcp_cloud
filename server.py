
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Trivial")


@mcp.tool()
def factorial(n: int) -> int:
    """Calcula el factorial de n"""
    if n < 0:
        raise ValueError("No se puede calcular factorial de un número negativo")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool()
def fibonacci(n: int) -> int:
    """Calcula el n-ésimo número de Fibonacci"""
    if n < 0:
        raise ValueError("El índice de Fibonacci no puede ser negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    mcp.run()   