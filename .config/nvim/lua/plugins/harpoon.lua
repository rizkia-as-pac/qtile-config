return {
	"theprimeagen/harpoon",

	config = function()
		local mark = require("harpoon.mark")
		local ui = require("harpoon.ui")

		vim.keymap.set("n", "<M-a>", mark.add_file)
		vim.keymap.set("n", "<M-s>", ui.toggle_quick_menu)

		vim.keymap.set("n", "<M-u>", function()
			ui.nav_file(1)
		end)
		vim.keymap.set("n", "<M-i>", function()
			ui.nav_file(2)
		end)
		vim.keymap.set("n", "<M-o>", function()
			ui.nav_file(3)
		end)
		vim.keymap.set("n", "<M-p>", function()
			ui.nav_file(4)
		end)
	end,
}
