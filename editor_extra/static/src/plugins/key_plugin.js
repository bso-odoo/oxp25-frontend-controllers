import { Plugin } from "@html_editor/plugin";

const KEY_RE = /^(Ctrl-|Alt-|Shift-)+(\w)$/g;

export class KeyPlugin extends Plugin {
    static id = "key";
    static dependencies = ["dom", "feff", "input", "selection"];
    /** @type {import("plugins").EditorResources} */
    resources = {
        on_input_handlers: this.onInput.bind(this),
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

