import { EMBEDDED_COMPONENT_PLUGINS, MAIN_PLUGINS } from "@html_editor/plugin_sets";
import { KeyPlugin } from "./plugins/key_plugin";
import { SpoilerPlugin } from "./plugins/spoiler_plugin";

MAIN_PLUGINS.push(KeyPlugin);
EMBEDDED_COMPONENT_PLUGINS.push(SpoilerPlugin);
