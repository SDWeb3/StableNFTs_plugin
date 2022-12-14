import modules.scripts as scripts
import gradio as gr

class Script(scripts.Script):

    def title(self):
        return "StableNFTs_plugin"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        NFT = gr.HTML("<style>.shannon_was_here {width: 100%; height:450px;}</style><hr><iframe id=\"frame\" class=\"shannon_was_here\" src=\"https://stable-nf-ts.vercel.app/index.html\"/><hr>")
        self.run_callback = False
        return [NFT]
        