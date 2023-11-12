<script>
	//import './styles.css';
	import '../style/app.css';
	import { writable, derived } from 'svelte/store';

	
	let repprenom = null;
	let repmdp = '';
	let repbenf = null;
	let reppp = null;
	
	const prenombd = () => {
		let error = null;
		

		fetch(`http://127.0.0.1:8000/prenom/${prenom}`, {
		method: 'GET',
		headers: {
			'accept': 'application/json'
		}
		})
		.then(response => response.json())
		.then(data => {
			repprenom = data;
		})
		.catch(err => {
			error = err;
		})
		
	};

	
	const mdpbd = () => {
		let error = null;

		fetch(`http://127.0.0.1:8000/mdp/${prenom}`, {
		method: 'GET',
		headers: {
			'accept': 'application/json'
		}
		})
		.then(response => response.json())
		.then(data => {
			repmdp = data;
		})
		.catch(err => {
			error = err;
		})

		
	};

	const recupbeneficiaire = () => {
		let error = null;

		fetch(`http://127.0.0.1:8000/beneficiaire/${prenom}`, {
		method: 'GET',
		headers: {
			'accept': 'application/json'
		}
		})
		.then(response => response.json())
		.then(data => {
			reppp= data;
		})
		.then(()=> {
			if(mdp === repmdp){
				codebon = true
			}
			else{
				codebon = false
			}

			if(repprenom!= 'null' && repmdp == mdp){
				afficher = true
			}
		})
		.catch(err => {
			error = err;
		})

		
		
	};

	
	let codebon;
	let afficher = false;
	let prenom = '';
	let mdp = '';
	$:console.log(prenom ==='' && mdp ==='');
	$:console.log(prenom)

	
	$:console.log(prenom ==='' && mdp ==='');
	$:console.log(prenombd);
	$:console.log(repmdp);

</script>

<div id='page' class="h-screen">
	<header>
		<p class="text-center text-2xl pt-5 "> Secret Santa famille <br/> Rabatel </p>
	</header>
	
	<main class=" items-center justify-center">

		{#if afficher == false}
			<div id='id' class=" flex flex-col items-center rounded-xl border-black ml-3 mt-4 px-7 py-4 shadow-md">
				<h1 class = "flex center"> <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"> Qui es-tu ? <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"></h1>
				<form on:submit class = "flex flex-col items-center">
					<label class ="mb-2 mt-3 flex"> Ton nom :
						<input bind:value={ prenom } class = "border border-1 rounded border-black ml-3 bg" type= 'text' name="prenom" maxlength="55" size="7" />
					</label>
			
					<label class ="mb-5"> Ton code :
						<input bind:value={ mdp } class = "border border-1 rounded border-black ml-3" type= 'password' name="code" maxlength="55" size="7" />
					</label>
					<button on:click = {mdpbd} on:click = {prenombd} on:click = {recupbeneficiaire} disabled={prenom==='' || mdp===''} type="submit" class = " text-center border border-1 rounded border-black w-fit px-2 flex " > Voir </button>
				</form>

				{#if repprenom === 'null'}
					<p> <br/> je crois que tu ne fais pas partie de ce secret Santa {repprenom} {repbenf} </p>
				{:else if codebon == false}
					<p> <br/> hopopop mauvais code... </p>
				{:else}
					<p> </p>
				{/if}

			</div>
		{:else}
			<div id='id' class=" flex flex-col items-center rounded-xl border-black ml-3 mt-4 px-7 py-4 shadow-md">
				<h1 class = "flex center"> <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"> Qui es-tu ? <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"></h1>
				<p> <br/> Tu as pour mission d'offrir </p>
				<p> un cadeau a {reppp} !!! </br> </p>
				<button on:click = {() => {afficher = false}} type="submit" class = " text-center border border-1 rounded border-black w-fit px-2 flex " > Retour </button>
			</div>
		
		{/if}
		
		
			
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