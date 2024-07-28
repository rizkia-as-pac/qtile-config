return {
	"catppuccin/nvim",
	name = "catppuccin",
	priority = 1000,

	config = function()
		require("catppuccin").setup({
			flavour = "mocha",
			color_overrides = {
				mocha = {
					base = "#12121d",
					mantle = "#12121d",
					crust = "#12121d",
				},
			},

			vim.cmd.colorscheme("catppuccin"),
		})
	end,
}
