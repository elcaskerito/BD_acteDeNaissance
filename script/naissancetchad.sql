-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : ven. 26 nov. 2021 à 12:06
-- Version du serveur :  10.4.18-MariaDB
-- Version de PHP : 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `naissancetchad`
--

-- --------------------------------------------------------

--
-- Structure de la table `nouveau_né`
--

CREATE TABLE `nouveau_né` (
  `id_nouveau_ne` int(11) NOT NULL,
  `Nom` varchar(150) NOT NULL,
  `prenom` varchar(150) NOT NULL,
  `situation_matrimoniale_pere` varchar(150) NOT NULL,
  `fonction_pere` varchar(150) NOT NULL,
  `nom_mere` varchar(150) NOT NULL,
  `situation_matrimoniale_mere` varchar(150) NOT NULL,
  `fonction_mere` varchar(150) NOT NULL,
  `sexe_enfant` varchar(150) NOT NULL,
  `date_de_naissance` varchar(150) NOT NULL,
  `lieu_de_naissance` varchar(150) NOT NULL,
  `heure_naissance` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `id_utilisateur` int(11) NOT NULL,
  `Nom` varchar(150) NOT NULL,
  `prenom` varchar(150) NOT NULL,
  `login` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `role` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `nouveau_né`
--
ALTER TABLE `nouveau_né`
  ADD PRIMARY KEY (`id_nouveau_ne`);

--
-- Index pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`id_utilisateur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
