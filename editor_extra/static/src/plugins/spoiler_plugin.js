import { Plugin } from "@html_editor/plugin";
import { _t } from "@web/core/l10n/translation";
import { renderToElement } from "@web/core/utils/render";

export class SpoilerPlugin extends Plugin {
    static id = "spoiler";
    static dependencies = ["dom", "history", "selection"];
    /** @type {import("plugins").EditorResources} */
    resources = {
        user_commands: [{
            id: "spoiler",
            description: _t("Spoiler"),
            icon: "help",
            run: () => {
                const selection = this.dependencies.selection.getEditableSelection();
                this.insertSpoilerElement({ text: selection.toString() || "Spoiler" });
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

    insertSpoilerElement(embeddedProps) {
        const embedEl = renderToElement("editor_extra.SpoilerBlueprint", {
            embeddedProps: JSON.stringify(embeddedProps),
        });
        this.dependencies.dom.insert(embedEl);
        this.dependencies.history.commit();
        this.dependencies.selection.setSelection({
            anchorNode: embedEl,
            anchorOffset: 1,
        });
    }
}

