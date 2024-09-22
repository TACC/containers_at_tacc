"""
PyTorch Matrix Multiplication Tests

Carlos del-Castillo-Negrete
carlosd@tacc.utexas.edu
"""
import torch
import click
from rich.console import Console
from rich.table import Table
import time
import matplotlib.pyplot as plt

console = Console()

def format_flops(flops):
    """Format FLOPS to appropriate unit (GFLOPS, TFLOPS, PFLOPS, etc.)"""
    units = ['', 'K', 'M', 'G', 'T', 'P', 'E']
    unit_index = 0
    while flops >= 1000 and unit_index < len(units) - 1:
        flops /= 1000
        unit_index += 1
    return f"{flops:.2f} {units[unit_index]}FLOPS"

def perform_matmul_test(size, device):
    try:
        # Calculate memory requirement
        memory_gb = (size * size * 4 * 2) / (1024**3)  # For two matrices, in GB
        console.print(f"Estimated memory requirement: [yellow]{memory_gb:.2f} GB[/yellow]")

        # Create matrices
        x = torch.rand(size, size, device=device)
        y = torch.rand(size, size, device=device)

        memory_size = x.element_size() * x.nelement() * 2 / (1024 ** 2)  # Size in MB

        # Warm-up run
        torch.matmul(x, y)
        
        # Timed run
        start_time = time.time()
        z = torch.matmul(x, y)
        torch.cuda.synchronize() if device.type == "cuda" else None
        end_time = time.time()

        computation_time = end_time - start_time

        # Performance metric (FLOPS)
        flops = 2 * size ** 3  # For matrix multiplication
        flops_per_second = flops / computation_time

        return {
            "Matrix Size": size,
            "Memory Size (GB)": memory_size / 1024,  # Convert MB to GB
            "Computation Time (s)": computation_time,
            "Performance": format_flops(flops_per_second),
            "Raw FLOPS": flops_per_second  # For plotting
        }
    except RuntimeError as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        return None

def plot_scaling(results):
    sizes = [result["Matrix Size"] for result in results if result is not None]
    flops = [result["Raw FLOPS"] for result in results if result is not None]

    plt.figure(figsize=(12, 8))
    plt.plot(sizes, flops, marker='o')
    plt.title("Scaling: Performance vs Matrix Size")
    plt.xlabel("Matrix Size")
    plt.ylabel("Performance (FLOPS)")
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    # Format y-axis labels
    def flops_formatter(x, pos):
        return format_flops(x)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(flops_formatter))
    
    plt.tight_layout()
    plt.savefig("scaling_plot.png")
    console.print("[green]Scaling plot saved as 'scaling_plot.png'[/green]")

@click.command()
@click.option('--sizes', default='2048,4096,8192', show_default=True,
              help='Comma-separated list of matrix sizes')
@click.option('--gpu/--no-gpu', is_flag=True, default=True, show_default=True, help='Use GPU if available')
def run_matmul_tests(sizes, gpu):
    console.print("[bold blue]PyTorch Matrix Multiplication Test for Large Matrices[/bold blue]")
    console.print(f"PyTorch version: [green]{torch.__version__}[/green]")

    device = torch.device("cuda" if gpu and torch.cuda.is_available() else "cpu")
    console.print(f"Using device: [green]{device}[/green]")

    if device.type == "cuda":
        console.print(f"CUDA version: [green]{torch.version.cuda}[/green]")
        console.print(f"GPU: [green]{torch.cuda.get_device_name(0)}[/green]")
        console.print(f"GPU Memory: [green]{torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB[/green]")

    # Parse sizes
    size_list = [int(size.strip()) for size in sizes.split(',')]

    # Prepare results table
    table = Table(title="Matrix Multiplication Test Results")
    table.add_column("Matrix Size", style="cyan")
    table.add_column("Memory Size (GB)", style="magenta")
    table.add_column("Computation Time (s)", style="yellow")
    table.add_column("Performance", style="green")

    # Run tests for each size
    results = []
    for size in size_list:
        console.print(f"\nRunning test for matrix size: [bold]{size}x{size}[/bold]")
        result = perform_matmul_test(size, device)
        if result:
            results.append(result)
            table.add_row(
                f"{result['Matrix Size']}x{result['Matrix Size']}",
                f"{result['Memory Size (GB)']:.2f}",
                f"{result['Computation Time (s)']:.4f}",
                result['Performance']
            )
        else:
            console.print(f"[bold red]Test failed for size {size}x{size}. Skipping to next size.[/bold red]")

    # Display results table
    console.print(table)

    # Plot scaling results
    if results:
        plot_scaling(results)
    else:
        console.print("[bold red]No successful tests to plot.[/bold red]")

if __name__ == "__main__":
    run_matmul_tests()
