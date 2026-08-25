# `tmjsoncontract.datajson.plan_id`

- Read-only. `name` es texto almacenado; no se interpreta.
- En Bronze **no hay columna** llamada `plan_id` (0 columnas).

## Origen

| métrica | valor |
|---|---:|
| filas contrato | 10998 |
| `plan_id` vacío | 0 |
| distinct | **109** |
| longitud | 36 |
| cardinalidad contratos → plan_id | **N:1** (1–5848 contratos / plan) |

## Maestra observada

`tmjsonplan_server` filtrada `tipo='P'`. Join: `datajson.plan_id` = `tmjsonplan_server.datajson.id`.

| métrica | valor |
|---|---:|
| filas tipo P | 282 (id JSON único) |
| filas tipo S | 27 (sin overlap con plan_id) |
| cobertura de los 109 plan_id | **100%** |
| solo en maestra (P, sin contrato) | 173 |
| solo en contratos | 0 |
| `tmjsonplan_server.id` integer = `datajson.id` | 0/309 |

`maproductos.idproducto` y el resto de `idproducto`/`idservicio`/`idplantilla`: overlap **0**.

## Contratos por plan_id (109)

| plan_id | contratos | name almacenado |
|---|---:|---|
| `f5d03da9-737e-406f-8871-70e10c07cd88` | 5848 | Internet Residencial Proyecto Mintic 25 Megas |
| `1b3ca4bb-49b6-4f5a-8a91-30e25aa1b936` | 836 | Internet Residencial Proyecto Mintic Flex 150M Down 75 Up |
| `88a140ef-8c4b-4971-a2af-d7205a90a38d` | 769 | Internet Residencial MFOR T1 (20Mb) |
| `15af2109-b24c-415c-b385-fe12dbada1d5` | 523 | Internet Residencial MFOR T2 (30Mb) |
| `36738247-ba87-4261-b8bb-755bfcc660d5` | 478 | Internet Residencial MFOR T3 (40Mb) |
| `67a27332-4e19-4199-af19-b57962087bae` | 274 | Internet Residencial MFOR T4 (50Mb) |
| `29426a1b-aad3-4df5-ba26-959a782c027a` | 231 | Internet Residencial Proyecto Mintic Promo 80 |
| `975d120d-3785-43cb-9013-05f85a847e41` | 219 | Internet Residencial Hatonuevo FOR T1 (10Megas) |
| `a36578a8-d29a-41f6-9afa-52228e699d55` | 170 | Internet Residencial Standard Fibra Optica T1 (150Mb) |
| `d67d3c6e-361f-4fc4-a34e-17d323dcaab9` | 131 | Internet Residencial MFOR T5 (60Mb) |
| `0ca7082f-6863-4ed2-8d96-169451765cc0` | 125 | Internet Residencial Hatonuevo FOR T2 (15Megas) |
| `aea879ff-872f-40b2-a76e-eb04acf96c50` | 114 | Internet Residencial Hatonuevo FOR T3 (25Megas) |
| `c02d76cb-a951-4952-a67c-95ba37ac1d53` | 112 | Internet Residencial Corregimiento Locales FOR T2 (10Megas) |
| `100a5b86-f92e-4f85-82ac-5074b8009146` | 90 | Internet Residencial Corregimiento Locales FOR T3 (15Megas) |
| `4959734d-1a2f-491e-bf59-7fbf83237764` | 84 | Internet Residencial Fibra Optica Municipal T1 (40 Megas) |
| `0cd83d79-8443-4b60-a160-69656025147c` | 71 | Internet Residencial Ciudad Capital FOR T1 (250Megas) |
| `eaa80419-ef19-49eb-a1f6-50349abc73a3` | 58 | Internet Residencial MFOR T6 (80Mb) |
| `f2c2a26c-f78c-467e-bb90-fca289983ded` | 54 | Internet Comercial MFOR T1 (30Mb) |
| `dbd4e942-90eb-4695-b3de-c483771415c2` | 51 | Internet Residencial MFOR T7 (100Mb) |
| `1d220b79-515f-476d-b01a-26b57806baf1` | 49 | Internet Residencial Ciudad Capital S FOR T1 (150Megas) |
| `00c7c848-d6ba-4fa9-a339-b5a0fb599be6` | 45 | Internet Empresarial MFOR T1 (50Mb) |
| `38e4dde9-d360-48fc-8e8f-b9e218e94a9e` | 44 | Internet Empresarial MFOR T3 (100Mb) |
| `e6ce8e0e-d60e-4d77-823b-61886bd66481` | 34 | Internet Empresarial Fibra Optica Municipal T1 (150 Megas) |
| `33871d68-f4a9-46e9-929a-adf90891f572` | 29 | Internet Residencial MFOR T4 (50Mb) Duplicado |
| `b0aceda7-3cac-46fb-8cb5-d7d5e129b9d2` | 27 | Internet Residencial Rural FOR T1 (10Megas) |
| `d51a21fe-5171-4277-969a-fbaa2d3a945f` | 25 | Internet Residencial Corregimiento Locales FOR T4 (20Megas) |
| `1a4abfcf-3d56-45d5-85b7-cdb05e7881d7` | 24 | Internet Empresarial MFOR T2 (80Mb) |
| `36bb33a3-d57d-4dc0-9045-f7f0754c0dd6` | 22 | Internet Residencial Ciudad Capital FOR T2 (400Megas) |
| `0b72447d-d6be-4eaa-8e46-fe49e7cbd83f` | 21 | Internet Residencial Hatonuevo FOR T5 (40Megas) |
| `a2840979-2004-470c-b0a4-babd5ee8a84c` | 21 | Internet Residencial Rural FOR T3 (20Megas) |
| `4e179a64-4d10-4cef-b69a-095ea97f426c` | 20 | Internet Dedicado FOR T2 (20Megas) |
| `75704f84-ade0-40d5-b14f-031fdb15e7e3` | 20 | Internet Dedicado FOR T5 (50Megas) |
| `237b1b66-7aa8-4a52-a058-6996ca5fa56c` | 19 | Internet Residencial Rural FOR T2 (15Megas) |
| `9ad87679-1972-41db-a67d-5f70594eb511` | 18 | Internet Residencial Ciudad Capital FOR T3 (550Megas) |
| `77c6a592-ca4d-4a65-932f-4a64278f49c9` | 15 | Internet Residencial Standard Fibra Optica T2 (300Mb) |
| `e5d79686-3129-447d-a9aa-65090849881b` | 15 | Internet Comercial MFOR T2 (40Mb) |
| `2488bbce-a3a6-40a8-a919-720cbefe2739` | 14 | Internet Residencial MFOR T5 (60Mb) Duplicado |
| `02674d7e-25ee-4c2e-83d3-8202db5de8b8` | 13 | Internet Comercial MFOR T3 (50Mb) |
| `09cbc562-73a7-42fa-b226-819f5d3bf7bf` | 13 | Internet Residencial Hatonuevo FOR T4 (30Megas) |
| `55eab923-cb8c-4677-8ea0-3721a2ac40c2` | 12 | Internet Empresarial MFOR T5 (200Mb) |
| `f2154b34-95c4-422c-b5d7-95ab0818d93e` | 12 | Internet Dedicado FOR T1.5 (15Megas) |
| `534b653a-1d6f-4b9a-9c34-21b1b74a2908` | 11 | Internet Empresarial MFOR T4 (150Mb) |
| `6121729a-a282-4a7e-86cc-34eb90611a08` | 11 | Internet Residencial Subsidiado |
| `1b93156c-c544-4dff-8ef2-062c1876c1e8` | 10 | Internet Residencial Corregimiento Locales FOR T5 (30Megas) |
| `54961929-25e3-41d8-8773-c3996841e25d` | 10 | Internet Residencial Proyecto Mintic Basic 150M Down 75 Up |
| `83b197d9-22ee-4499-8125-1617743a83b4` | 10 | Internet Dedicado FOR T1 (10Megas) |
| `91b236da-e097-4e91-a385-188a6dcaf1dc` | 10 | Internet Residencial Corregimiento Locales FOR T1 (8Megas) |
| `e46c6d66-f2ca-47b7-a9a4-9c5d1260b7b5` | 10 | Internet Residencial Ciudad Capital FOR T4 (650Megas) |
| `24209be9-654a-481e-bc78-d2b6aab0fe6c` | 9 | Internet Residencial MFOR T8 (150Mb) |
| `7fca91f6-ece7-4cf6-b388-e947c09d33ff` | 9 | Internet Residencial Standard Fibra Optica T3 (250Mb) |
| `a664a8b3-0a21-4e8e-b6f5-42ce404c4886` | 8 | Internet Residencial MFOR T6 (80Mb) Duplicado |
| `17c80daa-4638-460b-b60f-8f1fc01d7a5e` | 7 | Internet Dedicado FOR T6 (100Megas) |
| `4a3585a6-d037-41b5-a5da-3a3796253976` | 7 | Internet Residencial Fibra Optica Municipal T2 (60 Megas) |
| `dbeb0632-ba63-4dfa-8306-a542231fbf87` | 7 | Internet Dedicado FOR T3 (30Megas) |
| `bbd4ed04-ec65-411d-bdfa-fea4dc3d79c1` | 6 | ----->DEDICADO<------ |
| `1303ce80-27a2-4b3e-b056-b6cd72d66c65` | 5 | Internet Empresarial MFOR T9 (400Mb) |
| `8760d852-644b-4906-9215-32853e0a0571` | 5 | Internet Empresarial MFOR T6 (250Mb) |
| `a8c02a79-002c-4d6c-afc3-b75efce6445d` | 5 | Internet Dedicado FOR T4 (40Megas) |
| `c8aebdfc-ea3e-4df0-8c0a-752f25a82c77` | 5 | Internet Residencial MFOR T7 (100Mb) Duplicado |
| `f717e5b9-0f81-4c53-b62f-8376c6c3dfce` | 5 | Internet Residencial Standard Fibra Optica T4 (400Mb) |
| `821693bb-fb47-4226-a943-8188398e7bf2` | 4 | Internet Empresarial Fibra Optica Municipal T4 (300 Megas) |
| `9511ed3c-fde8-40cf-8e3e-427edf0e214f` | 4 | Internet Rural Casa Finca Radio T2 (20Megas) |
| `d665a464-8fa5-4e8b-81de-dfff68d506d8` | 4 | Internet Residencial Rural FOR T4 (30Megas) |
| `f9dc7380-b91f-4d9c-b0d8-8a67273261c7` | 4 | Internet Empresarial Fibra Optica Municipal T5 (400 Megas) |
| `01337a78-5027-464c-b3b2-dc4a7aa6750b` | 3 | Proyecto Internet Down 10M up 5M |
| `205076fc-1bcb-43cb-9817-20d648231945` | 3 | Internet Empresarial MFOR T8 (350Mb) |
| `2bce2ed7-7f8b-4a2f-9f71-8f295261744e` | 3 | Internet Comercial Fibra Optica Municipal T1 (100 Megas) |
| `4763a564-e527-43a1-bb67-dacd0b3ebcbf` | 3 | Internet Residencial MFOR T9 (200Megas) Duplicado |
| `54311fc4-fab5-4232-a6e0-244241acbec9` | 3 | Internet Dedicado FOR T8 (300Megas) |
| `6798d6a0-e10b-4786-a8ff-bb991fcef07f` | 3 | Internet Residencial Fibra Optica Municipal T4 (150 Megas) |
| `878d270e-e25a-43a0-b564-f75378ebbc4c` | 3 | Internet Dedicado FOR T (500Megas) |
| `bc101d79-075d-4024-81e4-0ef828643550` | 3 | Internet Residencial Fibra Optica Municipal T3 (100 Megas) |
| `cfbe84aa-8f29-4ebc-a189-34edf89cd3fe` | 3 | Internet Residencial MFOR T9 (200Mb) |
| `e607af31-396b-428a-9ffe-00beb291a9a0` | 3 | Internet Comercial Corregimiento Locales FOR T2 (15Megas) |
| `f148f2bd-238c-494f-970b-54ec2a7bacbe` | 3 | Internet Empresarial Fibra Optica Municipal T2 (200 Megas) |
| `17f6257c-7db5-4178-a2f9-71519fbc626f` | 2 | Internet Empresarial Municipales-Corregimiento-Locales FOR T4 (30Megas) |
| `1cf6cd19-c7b3-4db3-9837-cca1a302e631` | 2 | Internet Residencial MFOR T1 (20Mb) Duplicado |
| `47e285bd-6093-40e9-ac5d-adedc5150499` | 2 | Internet Residencial MFOR T8 (150Megas) Duplicado |
| `5eb6b632-a034-4d28-80c9-2423374e3d82` | 2 | Internet Empresarial Fibra Optica Municipal T6 (500 Megas) |
| `89c90bce-fb18-4613-988d-8e1d05c31665` | 2 | Internet Residencial Fibra Optica Municipal T5 (200 Megas) |
| `8d5e96f6-ac61-40b0-a9f7-57ef57c0505b` | 2 | Internet Rural Casa Finca Radio T1 (10Megas) |
| `9518b40f-48fb-4108-8d4a-7fb0720475bf` | 2 | Canal de Internet Alta Disponibilidad Cerrejon (1200 MB) |
| `9f2960b9-02c3-4a07-9318-048083db426f` | 2 | Internet Empresarial MFOR T7 (300Mb) |
| `b9b4a4ed-c854-4d86-aec9-8249bf3c7724` | 2 | Internet Residencial Hatonuevo FOR T8 (100Megas) |
| `d3de0703-af9e-4159-9403-04417e4f75c0` | 2 | Internet Dedicado FOR T9 (400Megas) |
| `d9d3308c-dd1a-40f6-94c9-a66d232d5f7c` | 2 | Canal de Internet Alta Disponibilidad Cerrejon (700 MB) |
| `db594f1a-1535-4938-b714-ece239b634b6` | 2 | Canal de Internet Alta Disponibilidad Cerrejon (1500 MB) |
| `e525bd61-591d-46fb-94c9-f2049c97d3bd` | 2 | Canal de Internet Alta Disponibilidad Cerrejon (1000 MB) |
| `e8ce4195-2ee0-4c00-bff6-85dd70b969e4` | 2 | Internet Dedicado FOR T7 (200Megas) |
| `ff4908e9-1490-442f-ac7a-1f39c852a57d` | 2 | Internet Empresarial Fibra Optica Municipal T8 (700 Megas) |
| `092da124-9136-4d11-8f48-36a3776723d7` | 1 | Internet Dedicado FOR (2000M) |
| `112370ea-6d6b-4ad2-8c71-2e9513aa02e1` | 1 | Internet Empresarial FOR T5 (30Megas) |
| `12d1aaac-4e4b-46e9-b451-4a42df6f9106` | 1 | Internet Semi-Dedicado FOR T1 (100Megas) |
| `1809def7-8d44-41f4-86ce-aa2dfacf16b0` | 1 | Internet Residencial Standard Fibra Optica T7 (900Mb) |
| `1c2153fe-074a-49af-8c20-65041f85c8b1` | 1 | Internet Residencial Standard Fibra Optica T5 (500Mb) |
| `227fcec2-5497-42f9-8294-93c24cfa2036` | 1 | Internet Comercial Ciudad Capital S FOR T1 (200Megas) |
| `30fc1f32-07c5-4587-997e-0b02fc170294` | 1 | Internet Empresarial Fibra Optica Municipal T3 (250 Megas) |
| `5dfd69a4-b020-4358-9439-7aeccea33df8` | 1 | Canal de Internet Alta Disponibilidad Cerrejon (1100 MB) |
| `6cbde7b7-919f-4886-839f-80c80bad4732` | 1 | Internet Residencial Hatonuevo FOR T7 (80Megas) |
| `8388142b-b7a3-4f94-be43-e216da8b8155` | 1 | Internet Residencial Corregimiento Locales FOR T7 (50Megas) |
| `8ca4d7ea-1324-42f8-8d64-059d231c05aa` | 1 | Internet Dedicado FOR T9 (150Megas) |
| `9e5eaba6-5e4e-4550-bf66-5a7b824e093d` | 1 | Internet Comercial MFOR T4 (80Mb) |
| `afe9a200-295e-44e3-bfc5-97b03f460cd1` | 1 | Dedicado 80 Mb |
| `c05cb8bd-893e-4273-b3e7-199148a95880` | 1 | Internet Residencial MFOR T3 (40Mb) Duplicado |
| `c17cdedf-1e30-4ffc-a7c4-e61cae3400ce` | 1 | Internet Comercial Fibra Optica Municipal T2 (150 Megas) |
| `cb57c750-115f-4904-b304-f24b1b981327` | 1 | Internet Dedicado FOR T25 (250Megas) |
| `d6fe4674-d7b0-4ea6-80d9-7c0da5b79c57` | 1 | Internet Empresarial Fibra Optica Municipal T7 (600 Megas) |
| `f2e4c4f0-ea92-47e9-9304-5ac88ede64e4` | 1 | Internet Comercial Ciudad Capital S FOR T2 (300Megas) |
| `f70c3e6d-8fcf-42f7-946a-0baba1537991` | 1 | Internet Comercial FOR T7 (50Megas) |

JSON: `output/lookup_plan_id.json`
