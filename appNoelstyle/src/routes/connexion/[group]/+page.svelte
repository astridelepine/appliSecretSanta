<script>
	import '../../styles.css';
	import '../../../style/app.css';
	import {onMount, tick} from 'svelte';
	import {PUBLIC_URL_API} from '$env/static/public'

	/**
   * @type {string | null}
   */
	let repprenom = null;
	let repmdp = '';
	/**
   * @type {Response | boolean | null}
   */
	let repbenf = null;
	
	/**
   * @type {boolean | Response}
   */
	let user;
	let afficher = false;
	let prenom = '';
	let mdp = '';

	let url;
	let group;

	onMount (() => {
		url = window.location.href;
		group = url.split("/")[4];
	})
	 
	// const prenombd = async() => {
	// 	let error = null;
	// 	let response = await fetch(`https://noel-api.super-sympa.fr/prenom/${group}/${prenom}`);

	// 	response = await response.json();
	// 	repprenom = await response;
		
	// };

	
	// const mdpbd = async() => {
	// 	let error = null;
	// 	let response = await fetch(`https://noel-api.super-sympa.fr/mdp/${group}/${prenom}`);
		
	// 	response = await response.json();
	// 	repmdp = response;
		
	// };

	const userbd = async() => {
		let error = null;
		let response = await fetch(`${PUBLIC_URL_API}/user/${group}/${prenom}/${mdp}`);

		response = await response.json();
		if(response){
			repprenom = prenom;
			repbenf = response;
		} else {
			repprenom = 'null';
		}
		return response;
	};

	const recupbeneficiaire = async() => {
		let error = null;
		let response = await fetch(`${PUBLIC_URL_API}/beneficiaire/${group}/${prenom}`);

		response = await response.json();
		repbenf = response;
		console.log(repbenf);
		
	};

	const traitementbouton = async (e) => {
			e.preventDefault();
			user = await userbd();
			// await prenombd();
			// await mdpbd();
			try {
			const responseUser = await fetch(`${PUBLIC_URL_API}/user/${group}/${prenom}/${mdp}`);
			const userData = await responseUser.json();

			// const responseBenf = await fetch(`${PUBLIC_URL_API}/beneficiaire/${group}/${prenom}`);
			// const benfData = await responseBenf.json();

			if (!userData) {
				repprenom = null;
				user = false;
				repbenf = false;
			} else {
				repprenom = prenom;
				user = true;
				repbenf = userData;
				afficher = true;
			}

			console.log("repprenom:", repprenom);
			console.log("repbenf:", repbenf);


		} catch (err) {
			console.error(err);
		}
		};
	

</script>

<div id='page' class="h-screen">
	<header>
		<p id = "groupe" class="text-center text-2xl pt-5 "> {group}</p>
	</header>
	
	<main class=" items-center justify-center">

		{#if afficher == false}
			<div id='id' class=" flex flex-col items-center rounded-xl border-black ml-3 mt-4 px-7 py-4 shadow-md">
				<h1 class = "flex center"> <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"> Qui es-tu ? <img class="object-cover h-7 w-7" src="https://www.gifimili.com/gif/2018/05/smiley-guirlande-de-noel.gif"  alt="Smiley Guirlande de Noël"></h1>
				<form on:submit={traitementbouton} class = "flex flex-col items-center">
					<label class ="mb-2 mt-3 flex"> Ton nom :
						<input bind:value={ prenom } class = "border border-1 rounded border-black ml-3 bg" type= 'text' name="prenom" maxlength="55" size="7" />
					</label>
			
					<label class ="mb-5"> Ton code :
						<input bind:value={ mdp } class = "border border-1 rounded border-black ml-3" type= 'password' name="code" maxlength="55" size="7" />
					</label>
					<button disabled={prenom==='' || mdp===''} type="submit" class = " text-center border border-1 rounded border-black w-fit px-2 flex " > Voir </button>
				</form>

				{#if repbenf == false }	
					<p> <br/> Nom ou mdp incorect </p>
				<!-- {:else if user === false}
					<p> <br/> hopopop mauvais code... </p> -->
				{:else}
					<p> </p>
				{/if}

			</div>
		{:else}
			<div id='id' class=" flex flex-col items-center rounded-xl border-black ml-3 mt-4 px-7 py-4 shadow-md">
				<img class=" h-16 " src="https://www.gifimili.com/gif/2018/02/papa-noel-danse-avec-les-rennes.gif" alt="Papa Noël danse avec les rennes">
				<p> <br/> Tu as pour mission d'offrir </p>
				<p class = "mb-4"> un cadeau à {repbenf} !!! <br/> </p>
				
				<button on:click = {() => {afficher = false}} type="submit" class = " text-center border border-1 rounded border-black w-fit px-2 flex " > Retour </button>
			</div>
		
		{/if}
			
	</main>
	
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



	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>