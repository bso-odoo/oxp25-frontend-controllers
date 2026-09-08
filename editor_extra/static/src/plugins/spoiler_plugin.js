import { Plugin } from "@html_editor/plugin";
import { closestElement, selectElements } from "@html_editor/utils/dom_traversal";
import { _t } from "@web/core/l10n/translation";

export class SpoilerPlugin extends Plugin {
    static id = "spoiler";
    static dependencies = ["dom", "feff", "input", "selection"];
    /** @type {import("plugins").EditorResources} */
    resources = {
        user_commands: [{
            id: "spoiler",
            description: _t("Spoiler"),
            icon: "help",
            run: () => {
                alert("Called");
            },
            isAvailable: (selection) => {
                return true;
            },
        }],
        shortcuts: [{
            hotkey: "control+m",
            commandId: "spoiler",
        }],
        toolbar_groups: [{ id: "oxp" }],
        toolbar_items: [{
            id: "spoiler",
            description: _t("Spoiler (Ctrl+M)"),
            groupId: "oxp",
            namespaces: ["compact", "extended"],
            commandId: "spoiler",
            isActive: (selection, items) => {
                return false;
            },
            isDisabled: (selection, items) => {
                return false;
            },
        }],
        powerbox_categories: [{
            id: "oxp",
            name: _t("OXP"),
        }],
        powerbox_items: [{
            title: _t("Spoiler"),
            description: _t("Insert a spoiler"),
            icon: "help",
            categoryId: "oxp",
            commandId: "spoiler",
            keywords: [_t("hide"), _t("hidden")],
        }],
    };
}

