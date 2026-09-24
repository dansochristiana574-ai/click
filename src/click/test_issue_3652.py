import click
from click.testing import CliRunner

def test_multiple_option_ellipsis_in_help():
    @click.command()
    @click.option("--foo", multiple=True, help="A list of foo strings.")
    def cmd(foo):
        pass

    runner = CliRunner()
    result = runner.invoke(cmd, ["--help"])

    assert "--foo TEXT..." in result.output
