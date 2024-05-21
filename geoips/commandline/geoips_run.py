"""GeoIPS CLI "run" command.

Runs the appropriate script based on the args provided.
"""

from geoips.commandline.args import add_args
from geoips.commandline.run_procflow import main
from geoips.commandline.geoips_command import GeoipsCommand, GeoipsExecutableCommand
from data_fusion.commandline.args import add_args as data_fusion_add_args


class GeoipsRunConfigBased(GeoipsExecutableCommand):
    """Run Sub-Command for executing the config based process-workflow (procflow)."""

    name = "config_based"
    command_classes = []

    def add_arguments(self):
        """Add arguments to the run-subparser for the 'run config_based' Command."""
        add_args(parser=self.parser, legacy=self.legacy)

    def __call__(self, args):
        """Run the provided GeoIPS command.

        Parameters
        ----------
        args: Namespace()
            - The argument namespace to parse through
        """
        if args.procflow is None and self.legacy:
            err_str = (
                "Deprecated, Legacy 'run_procflow' call was used and --procflow "
                "flag wasn't specified. Please either specify which procflow is "
                "being executed via '--procflow <procflow_name>' or use the "
                "supported procflow call 'geoips run <procflow_name>'"
            )
            self.parser.error(err_str)
        elif args.procflow is None:
            # If None, set to 'config_based'. We don't want users to have to specify
            # what procflow will be used as it is specified in
            # 'geoips run config_based'.
            args.procflow = "config_based"
        main(ARGS=args)


class GeoipsRunDataFusion(GeoipsExecutableCommand):
    """Run Sub-Command for executing the data fusion process-workflow (procflow)."""

    name = "data_fusion"
    command_classes = []

    def add_arguments(self):
        """Add arguments to the run-subparser for the 'run data_fusion' Command."""
        data_fusion_add_args(parser=self.parser, legacy=self.legacy)

    def __call__(self, args):
        """Run the provided GeoIPS command.

        Parameters
        ----------
        args: Namespace()
            - The argument namespace to parse through
        """
        if args.procflow is None and self.legacy:
            err_str = (
                "Deprecated, Legacy 'data_fusion_procflow' call was used and "
                "--procflow flag wasn't specified. Please either specify which "
                "procflow is being executed via '--procflow <procflow_name>' or "
                "use the supported procflow call 'geoips run <procflow_name>'"
            )
            self.parser.error(err_str)
        elif args.procflow is None:
            # If None, set to 'data_fusion'. We don't want users to have to specify
            # what procflow will be used as it is specified in
            # 'geoips run data_fusion'.
            args.procflow = "data_fusion"
        main(ARGS=args)


class GeoipsRunSingleSource(GeoipsExecutableCommand):
    """Run Sub-Command for executing the single source process-workflow (procflow)."""

    name = "single_source"
    command_classes = []

    def add_arguments(self):
        """Add arguments to the run-subparser for the 'run single_source' Command."""
        add_args(parser=self.parser, legacy=self.legacy)

    def __call__(self, args):
        """Run the provided GeoIPS command.

        Parameters
        ----------
        args: Namespace()
            - The argument namespace to parse through
        """
        if args.procflow is None and self.legacy:
            err_str = (
                "Deprecated, Legacy 'run_procflow' call was used and --procflow "
                "flag wasn't specified. Please either specify which procflow is "
                "being executed via '--procflow <procflow_name>' or use the "
                "supported procflow call 'geoips run <procflow_name>'"
            )
            self.parser.error(err_str)
        elif args.procflow is None:
            # If None, set to 'single_source'. We don't want users to have to specify
            # what procflow will be used as it is specified in
            # 'geoips run single_source'.
            args.procflow = "single_source"
        main(ARGS=args)


class GeoipsRun(GeoipsCommand):
    """Run Sub-Command for running process-workflows (procflows)."""

    name = "run"
    command_classes = [
        GeoipsRunSingleSource,
        GeoipsRunDataFusion,
        GeoipsRunConfigBased,
    ]
