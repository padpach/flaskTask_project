/*
 Navicat Premium Data Transfer

 Source Server         : loca_mysql_flask
 Source Server Type    : MySQL
 Source Server Version : 50704
 Source Host           : localhost
 Source Database       : task

 Target Server Type    : MySQL
 Target Server Version : 50704
 File Encoding         : utf-8

 Date: 03/20/2015 17:14:57 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `tasks`
-- ----------------------------
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `due_date` date NOT NULL,
  `priority` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `tasks`
-- ----------------------------
BEGIN;
INSERT INTO `tasks` VALUES ('1', 'Revisar la Base de Afiliapp', '2015-12-12', '5', '0'), ('2', 'Be better man', '2015-01-01', '1', '1'), ('3', 'Ser Honesto', '2015-03-03', '5', '1'), ('4', 'Love Jas', '2015-01-03', '4', '1'), ('5', 'Go to Bar', '2015-12-04', '5', '1'), ('6', 'Setup Centos and Flask', '2015-04-01', '10', '1'), ('7', 'Comer con Jas', '2105-03-20', '9', '1'), ('8', 'Likes to Dany P', '2015-03-20', '10', '1'), ('9', 'Likes to Mano', '2015-12-12', '1', '1');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
