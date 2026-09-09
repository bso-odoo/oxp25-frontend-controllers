import { Component, props, types as t } from "@odoo/owl";
import { getEmbeddedProps, StateChangeManager, useEmbeddedState } from "@html_editor/others/embedded_component_utils";

export class EmbeddedSpoilerComponent extends Component {
    static template = "editor_extra.EmbeddedSpoiler";
    props = props({
        text: t.string(),
        host: t.object(),
    });
    setup() {
        this.state = useEmbeddedState(this.props.host);
        this.state.clicked = false;
    }
    onInput() {
        this.state.text = this.props.host.textContent;
        this.state.clicked = true;
    }
    onClick() {
        this.state.clicked = true;
    }
}

export const spoilerEmbedding = {
    name: "spoiler",
    Component: EmbeddedSpoilerComponent,
    getProps: (host) => ({ host, ...getEmbeddedProps(host) }),
    getStateChangeManager: (config) => new StateChangeManager(config),
};
