# Requirements Engineering

This page describes the UTAT Space Systems requirements framework. 

# Anatomy

A requirement is structured as follows:

<aside>
🏗️ [ID]: The [system] [qualifier] [description] to [rationale] as verified through [verification method]

</aside>

Where:

- ID: A unique symbol to identify the requirement
- System: The name of the system that is intended to meet this requirement
- Qualifier: A key term that specifies the degree to which the requirement must be met
- Description: The actual requirement description
- Rationale: An explanation as to why the requirement is necessary
- Verification Method: The verification plan used to verify that the requirement is satisfied

<aside>
👪 A requirement may have more than one parent. Such a requirement is referred to as a cross-cutting requirement because it cuts across the requirement tree. Interface requirements commonly have more than one parent

</aside>

Here’s an example of a valid requirement:

> OCEAN-Payload-SpatialResolution: The payload shall be able to image the Earth with a spatial resolution of 1m±0.25m  to enable the detection of narwhals swimming in the ocean that cause commotions, as verified through pool testing.
> 

Let’s describe some of these components in greater detail.

## ID

The ID syntax used on Space Systems is as follows:

<aside>
⭐ `Mission-System-KeyTerms`

</aside>

Where:

- `Mission`: The mission this requirement applies to
- `System`: The system this requirement applies to
- `KeyTerms`: Any key terms that would help readily identify the requirement at a glance

The `KeyTerms` are written in [PascalCase](https://www.theserverside.com/definition/Pascal-case). Why Pascal? Its just more visually consistent compared to the alternatives. Try to keep this to 2-3 words max to prevent the ID from becoming too long.

## Qualifiers

The following database contains the requirement qualifiers used on Space Systems. These are adapted from [RFC 2119](https://microformats.org/wiki/rfc-2119). You’ll notice this list is much shorter than the number of qualifiers described by the standard. This was done to simplify the framework, and reduce redundancy in our terminology.

- SHALL: The item is an absolute requirement of the specification. Requires formal verification evidence to establish proof that the requirement is met.
- SHOULD: There may exist valid reasons in particular circumstances to ignore the item, but the full implications must be understood and carefully weighed before choosing a different course. Does not require formal verification evidence.
- WILL: WILL is used to indicate a statement of fact. It is used to describe parameters or characteristics of a system that are fully constrained by the parent requirements. WILL requirements do not undergo a tradeoff study or any kind of decision making to derive. WILL statements are not subject to verification
- MAY: The item is allowable or permissible. This is useful for encoding regulatory or policy constraints into the requirements model. I.e. The spacecraft MAY conduct autonomous imaging as per policy XYZ if ABC conditions are met

<aside>
💡 If a requirement is not a “shall”, it’ll likely be ignored

</aside>

## Description

This is the actual statement that specifies what the requirement is. When specifying numerical performance requirements, one should also describe tolerances. In reality, no specification is perfect. A battery may produce 5.01V, so if the requirement for battery voltage is written as, “The battery shall produce 5V”, would the requirement be met? This is where it can be valuable to describe the requirement using tolerances, i.e., “The battery shall produce 5V±0.5V”. The origin for these tolerances should also be declared in the rationale.

The utility function of a requirement, if applicable, would be written here.

Unconfirmed requirements are written as To be Determined (TBD). Requirements behind NDAs or external sources can be written as links that point to the original source.

## Rationale

The rationale is an incredibly important piece of the requirements statement. Years into the program, you may not remember why the requirement was necessary (or may have moved to another project and left the team scratching their heads).

## Verification Methods

A requirement can be verified by one or more of these methods. The methods are somewhat hierarchical in nature, as each verifies requirements of a product or system with increasing rigor.

- Review: The review of documentation (i.e. design description documents, architectures, schematics, materials & parts lists, plans, procedures, etc.)
- Inspection: Physical observation through senses (i.e. sight, touch, feel, smell, taste). This includes activities like weighing a component to confirm the mass, measuring critical dimensions/clearances/tolerances, etc.
- Demonstration: Showing that the system can functionally complete the task required of the system. Demonstration is often used not only to verify system functional requirements, but to validate that the requirements actually achieve the mission needs. Pass/fail is defined as completion of the executing task/script/sequence.
- Analysis: Analytical exercise through calculations, modeling, or simulations to predict system performance within an acceptable uncertainty.
- Test: Performing a test to show that functional and performance requirements are met, with emphasis on collecting quantifiable data to verify performance parameters against a pre-defined pass/fail value. Using a controlled and predefined series of inputs, data, or stimuli to ensure that the product or system will produce a very specific and predefined output as specified by the requirements.

# Requirements for Requirements

Here we outline the basic rules all requirements follow. Good requirements are:

- **Singular**: requirements should have only one qualifier per requirement description to ensure the scope of the requirement is constrained
- **Unambiguous**: requirements should be written in a way that attempts to ensure there is only one possible interpretation. Acronyms shall be written out in full first
- **Verifiable**: requirements should be testable. If a requirement can’t be tested, its going to be impossible to determine whether the requirement was met
- **Necessary**: requirements should be unique and orthogonal. Avoid gold-plating your design with "nice to haves"
- **Sufficient**: combined, requirements should completely specify the system to be designed
- **Feasible**: requirements should be implementable within cost and schedule, and with currently attainable technology
- **Traceable**: requirements (with the exception of the root requirement) shall have at least one parent requirement. Orphan requirements indicate gold-plating or missing parent requirements. Circular references are not valid

Notice most of the above are SHOULD requirements. These are not hard and fast rules. The main objectives in requirements writing are 1) that your stakeholders interpret your requirements as you intended, and 2) that your requirements model is constructed in a way that makes it adaptable to future change (robust), without making them ambiguous. You do whatever you need to do to make that happen, even if it means straying from the conventional requirements guidelines.

# Workflow
Ask yourself,

> If someone gave me only this list of requirements and nothing else, could I completely design the system and have it meet its intended purpose?
> 

If the answer is yes, you’ve built a solid requirements model! 🎉