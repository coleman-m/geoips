"""Unit test for GeoIPS CLI `list-packages` command.

See geoips/commandline/ancillary_info/cmd_instructions.yaml for more information.
"""
import pytest

from tests.unit_tests.commandline.cli_top_level_tester import BaseCliTest


class TestGeoipsListPackages(BaseCliTest):
    """Unit Testing Class for GeoipsListPackages Command."""

    @property
    def all_possible_subcommand_combinations(self):
        """A list of every possible call signature for the GeoipsListPackages command.

        This includes failing cases as well.
        """
        if not hasattr(self, "_cmd_list"):
            self._cmd_list = [self._list_packages_args]
            # Add argument list which invokes the help message for this command
            self._cmd_list.append(["geoips", "list", "packages", "-h"])
            # Add argument list with a non-existent command call ("-p")
            self._cmd_list.append(
                ["geoips", "list", "packages", "-p", "geoips"]
            )
        return self._cmd_list

    def check_error(self, args, error):
        """Ensure that the 'geoips list-packages ...' error output is correct.

        Parameters
        ----------
        args: 2D list of str
            - The arguments used to call the CLI (expected to fail)
        error: str
            - Multiline str representing the error output of the CLI call
        """
        # bad command has been provided, check the contents of the error message
        assert args != ["geoips", "list", "packages"]
        usg_str = "usage: geoips [-h]"
        assert usg_str in error

    def check_output(self, args, output):
        """Ensure that the 'geoips list packages ...' successful output is correct.

        Parameters
        ----------
        args: 2D list of str
            - The arguments used to call the CLI
        output: str
            - Multiline str representing the output of the CLI call
        """
        if "usage: To use, type" in output:
            # -h has been called, check help message contents for this command
            assert args == ["geoips", "list", "packages", "-h"]
            assert "type `geoips list packages`" in output
        else:
            # The args provided are valid, so test that the output is actually correct
            assert args == ["geoips", "list", "packages"]
            # Assert that the correct headers exist in the CLI output
            headers = ["GeoIPS Package", "Docstring", "Package Path"]
            for header in headers:
                assert header in output
            # Assert that we found every installed package
            for pkg_name in self.plugin_packages:
                assert pkg_name in output

test_sub_cmd = TestGeoipsListPackages()

@pytest.mark.parametrize(
        "args",
        test_sub_cmd.all_possible_subcommand_combinations,
        ids=test_sub_cmd.generate_id,
)
def test_all_command_combinations(args):
    """Test all 'geoips list packages ...' commands.

    This test covers every valid combination of commands for the 'geoips list packages'
    command. We also test invalid commands, to ensure that the proper help documentation
    is provided for those using the command incorrectly.

    Parameters
    ----------
    args: 2D array of str
        - List of arguments to call the CLI with (ie. ['geoips', 'list', 'packages'])
    """
    test_sub_cmd.test_all_command_combinations(args)
