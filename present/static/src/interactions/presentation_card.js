import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

export class PresentationCard extends Interaction {
    static selector = ".presentation .card";
    dynamicContent = {
        ".card-text": {
            "t-on-click": async (ev) => {
                const el = ev.target.closest("[data-presentation]");
                if (el) {
                    const metadata = await this.waitFor(rpc(
                        "/present/metadata",
                        {
                            presentation_id: parseInt(el.dataset.presentation),
                        }
                    ));
                    this.services["notification"].add(`Written by ${metadata.author} on ${metadata.date}`, { type: "info" });
                }
            },
        },
    };
}

registry
    .category("public.interactions")
    .add("present.presentation_card", PresentationCard);
