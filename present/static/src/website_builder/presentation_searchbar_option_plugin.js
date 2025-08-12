import { Plugin } from "@html_editor/plugin";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

export class PresentationSearchbarOptionPlugin extends Plugin {
    static id = "presentationSearchbarOption";

    resources = {
        searchbar_option_order_by_items: [
            {
                label: _t("Date (old to new)"),
                orderBy: "write_date asc, id asc",
                dependency: "search_presentations_opt",
            },
            {
                label: _t("Date (new to old)"),
                orderBy: "write_date desc, id desc",
                dependency: "search_presentations_opt",
            },
        ],
        searchbar_option_display_items: [
            {
                label: _t("Description"),
                dataAttribute: "displayDescription",
                dependency: "search_presentations_opt",
            },
        ],
    };
}

registry.category("website-plugins").add(PresentationSearchbarOptionPlugin.id, PresentationSearchbarOptionPlugin);
