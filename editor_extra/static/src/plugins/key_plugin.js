import { Plugin } from "@html_editor/plugin";
import { closestElement, selectElements } from "@html_editor/utils/dom_traversal";

const KEY_RE = /^(Ctrl-|Alt-|Shift-)+(\w)$/g;

export class KeyPlugin extends Plugin {
    static id = "key";
    static dependencies = ["dom", "feff", "input", "selection"];
    /** @type {import("plugins").EditorResources} */
    resources = {
        on_input_handlers: this.onInput.bind(this),

        feff_providers: (root, cursors) =>
            selectElements(root, "kbd").flatMap((code) =>
                this.dependencies.feff.surroundWithFeffs(code, cursors)
            ),

        would_feff_be_legit_predicates: (node) => {
            if (
                (node.previousSibling && closestElement(node.previousSibling)?.nodeName === "KBD") ||
                (node.nextSibling && closestElement(node.nextSibling)?.nodeName === "KBD")
            ) {
                return true;
            }
        },
    };

    onInput(ev) {
        if (ev.data === " ") {
            const selection = this.dependencies.selection.getEditableSelection();
            let text = selection.focusNode.textContent.substring(0, selection.focusOffset - 1);
            text = text.replaceAll(/.*\s/g, "").replaceAll("+", "-");
            if (KEY_RE.test(text)) {
                // set selection on replaced text
                this.dependencies.selection.setSelection({
                    anchorNode: selection.focusNode,
                    anchorOffset: selection.focusOffset - text.length - 1,
                    focusNode: selection.focusNode,
                    focusOffset: selection.focusOffset,
                });
                // replace nodes with new content
                const fragment = this.document.createDocumentFragment();
                for (const part of text.split("-")) {
                    const kbdEl = this.document.createElement("kbd");
                    kbdEl.textContent = part;
                    fragment.append(kbdEl);
                    fragment.append(this.document.createTextNode(part.length === 1 ? " " : "+"));
                }
                this.dependencies.dom.insert(fragment);
            }
        }
    }
}

