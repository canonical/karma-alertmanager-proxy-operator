#!/usr/bin/env python3
# Copyright 2021 Canonical Ltd.
# See LICENSE file for licensing details.

"""Proxy charm for providing alertmanager URL info to Karma."""

import logging
import typing

from charms.karma_k8s.v0.karma_dashboard import KarmaProvider
from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus, BlockedStatus

logger = logging.getLogger(__name__)


class KarmaAlertmanagerProxyCharm(CharmBase):
    """A Juju charm for "proxying" a remote alertmanager for Karma."""

    _relation_name = "karma-dashboard"
    _service_name = "karma"

    def __init__(self, *args):
        super().__init__(*args)

        self.karma_provider = KarmaProvider(self, self._relation_name)

        # Core lifecycle events
        self.framework.observe(self.on.config_changed, self._on_config_changed)

    def _update_unit_status(self):
        """Helper function for updating the unit's status holistically."""
        if not self.karma_provider.target:
            self.unit.status = BlockedStatus(
                "Waiting for 'juju config url=...' with alertmanager url"
            )
            return

        self.unit.status = ActiveStatus(f"Proxying {self.karma_provider.target}")

    def _on_config_changed(self, _):
        """Event handler for ConfigChangedEvent."""
        # FIXME add option to clear the config and have the charm go back into BlockedState
        if url := self.config.get("url"):
            logger.debug("url = %s", url)

            self.karma_provider.target = typing.cast(str, url)

        self._update_unit_status()


if __name__ == "__main__":
    main(KarmaAlertmanagerProxyCharm, use_juju_for_storage=True)
