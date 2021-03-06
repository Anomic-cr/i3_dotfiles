"  __   __   __     __    __    
" /\ \ / /  /\ \   /\ "-./  \   
" \ \ \'/   \ \ \  \ \ \-./\ \  
"  \ \__|    \ \_\  \ \_\ \ \_\ 
"   \/_/      \/_/   \/_/  \/_/ 
"
" https://github.com/anomic-cr                             

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Plugins
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin('~/.vim/plugged')

	" Nord theme
	Plug 'arcticicestudio/nord-vim'
	"Catppuccin theme
	Plug 'catppuccin/nvim', {'as': 'catppuccin'}
	" File manager
	Plug 'scrooloose/nerdtree'
	" Status bar
	Plug 'vim-airline/vim-airline'
	" Rainbow parentheses
	Plug 'frazrepo/vim-rainbow'
	" Icons
	Plug 'ryanoasis/vim-devicons'
	" Preview CSS colors
	Plug 'ap/vim-css-color'
	" Multiple cursor
	Plug 'mg979/vim-visual-multi', {'branch': 'master'}

call plug#end()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General Settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set mouse=a
set cursorline
set cursorcolumn
set number relativenumber
syntax on
colorscheme catppuccin
let g:airline_powerline_fonts=1
let g:rainbow_active = 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Keybindings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <C-t> :NERDTreeToggle <CR>
nnoremap <C-s> :w <CR>
nnoremap <C-q> :wq <CR>


