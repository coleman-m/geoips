"""Unit test for GeoIPS CLI `list interfaces` command.

See geoips/commandline/ancillary_info/cmd_instructions.yaml for more information.
"""

import pytest

from tests.unit_tests.commandline.cli_top_level_tester import BaseCliTest


class TestGeoipsListInterfaces(BaseCliTest):
    """Unit Testing Class for List Interfaces Sub-Command."""

    @property
    def all_possible_subcommand_combinations(self):
        """A list of every possible call signature for the GeoipsListInterfaces command.

        This includes failing cases as well.
        """
        if not hasattr(self, "_cmd_list"):
            self._cmd_list = [self._list_interfaces_args]
            for pkg_name in self.plugin_package_names:
                self._cmd_list.append(
                    self._list_interfaces_args + ["-i", "-p", pkg_name]
                )
            # Add argument list which invokes the help message for this command
            self._cmd_list.append(["geoips", "list", "interfaces", "-h"])
            # Add argument list with an invalid command call ("-p" w/out "-i")
            self._cmd_list.append(["geoips", "list", "interfaces", "-p", "geoips"])
        return self._cmd_list

    def check_error(self, args, error):
        """Ensure that the 'geoips list interfaces ...' error output is correct.

        Parameters
        ----------
        args: 2D list of str
            - The arguments used to call the CLI (expected to fail)
        error: str
            - Multiline str representing the error output of the CLI call
        """
        # bad command has been provided, check the contents of the error message
        assert args != ["geoips", "list", "interfaces"]
        assert args != ["geoips", "list", "interfaces", "-i"]
        assert "usage: To use, type `geoips list interfaces`" in error
        assert "You cannot use the `-p` flag without the `-i` flag." in error

    def check_output(self, args, output):
        """Ensure that the 'geoips list interfaces ...' successful output is correct.

        Parameters
        ----------
        args: 2D list of str
            - The arguments used to call the CLI
        output: str
            - Multiline str representing the output of the CLI call
        """
        if "usage: To use, type" in output:
            # -h has been called, check help message contents for this command
            assert args == ["geoips", "list", "interfaces", "-h"]
            assert "To use, type `geoips list interfaces`" in output
        else:
            # The args provided are valid, so test that the output is actually correct
            if "-i" in args or "-p" in args:
                headers = ["GeoIPS Package", "Interface Type", "Interface Name"]
            else:
                # `geoips list-interfaces` was called, check for the correct headers
                headers = [
                    "GeoIPS Package",
                    "Interface Type",
                    "Interface Name",
                    "Supported Families",
                    "Docstring",
                    "Absolute Path",
                ]
            # Assert that the correct headers exist in the CLI output
            for header in headers:
                assert header in output


test_sub_cmd = TestGeoipsListInterfaces()


@pytest.mark.parametrize(
    "args",
    test_sub_cmd.all_possible_subcommand_combinations,
    ids=test_sub_cmd.generate_id,
)
def test_all_command_combinations(args):
    """Test all 'geoips list interfaces ...' commands.

    This test covers every valid combination of commands for the
    'geoips list interfaces' command. We also test invalid commands, to ensure that
    the proper help documentation  is provided for those using the command incorrectly.

    Parameters
    ----------
    args: 2D array of str
        - List of arguments to call the CLI with (ie. ['geoips', 'list', 'interfaces'])
    """
    test_sub_cmd.test_all_command_combinations(args)
