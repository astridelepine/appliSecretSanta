<script>
	//import './styles.css';
	import '../style/app.css';
	import { writable, derived } from 'svelte/store';

	let prenom = '';
	let mdp = '';
	$:console.log(prenom ==='' && mdp ==='');
</script>

<div id='page' class="h-screen">
	<header>
		<p class="text-center text-2xl pt-5 "> Secret Santa famille <br/> Rabatel </p>
	</header>
	
	<main class=" items-center justify-center">
		
		<div id='id' class=" flex flex-col items-center rounded-xl border-black ml-3 mt-4 px-7 py-4 shadow-md">
			<h1 class = "flex center"> <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"> Qui es-tu ? <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"></h1>
			<form on:submit class = "flex flex-col items-center">
				<label class ="mb-2 mt-3 flex"> Ton nom :
					<input bind:value={ prenom } class = "border border-1 rounded border-black ml-3 bg" type= 'text' name="prenom" maxlength="55" size="7" />
				</label>
		
				<label class ="mb-5"> Ton code :
					<input bind:value={ mdp } class = "border border-1 rounded border-black ml-3" type= 'password' name="code" maxlength="55" size="7" />
				</label>
				<button disabled={prenom ==='' && mdp === ''} type="submit" class = " text-center border border-1 rounded border-black w-fit px-2 flex " > Voir </button>
			</form>
		</div>
			
	</main>
	
	<footer>

	</footer>
</div>

<style>

	#page {
		background-color: #ececec;
	}

	#id, input{
		background-color: #fffcfc;
	}
	
	button{
		background-color: #eaeaea;
	}

	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
